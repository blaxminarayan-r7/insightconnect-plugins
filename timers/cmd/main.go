package main

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"os/signal"
	"strings"
	"syscall"

	"github.com/rapid7/komand-plugin-sdk-go2/cli"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugin-sdk-go2/message"
	"github.com/rapid7/komand-plugins/timers/actions"
	"github.com/rapid7/komand-plugins/timers/connection"
	"github.com/rapid7/komand-plugins/timers/server/http"
	"github.com/rapid7/komand-plugins/timers/triggers"
	kingpin "gopkg.in/alecthomas/kingpin.v2"
)

var (
	// Name plugin name
	Name = "timers"
	// Vendor plugin vendor
	Vendor = "rapid7"
	// Version plugin version
	Version = "2.0.2"
	// Description plugin description
	Description = "A variety of time-based triggers"
	// DefaultPort is the default port to use
	DefaultPort = "10001"
)

// getMessageFromStdin looks through both stdin and the os.Args for a message body to work as input
func getMessageFromStdin() (*message.V1, *message.BodyV1, error) {
	b := &message.BodyV1{}
	m := &message.V1{
		Body: b, // Seed it with a type so marshalling works
	}
	dec := json.NewDecoder(os.Stdin)
	if err := dec.Decode(m); err != nil {
		// Try from os.Args[3] which is where the komand engine code will send the data
		// when it's not over stdin - this will always have a "--" in pos 2
		if len(os.Args) == 4 && os.Args[2] == "--" {
			if err := json.Unmarshal([]byte(os.Args[3]), m); err != nil {
				return nil, nil, err
			}
			return m, b, nil
		}
		// If it wasn't over stdin, and it wasn't in pos3, following "--" in pos2, it's an error
		return nil, nil, fmt.Errorf("Unable to find message in os.Stdin nor os.Args: %+v", os.Args)
	}
	return m, b, nil
}

func main() {
	app := kingpin.New(Name, Description)
	app.Version(Version)

	debug := app.Flag("debug", "Log events to stdout.").Default("false").Bool()
	test := app.Command("test", "Run a test using the start message over STDIN.")
	info := app.Command("info", "Display plugin info (triggers and actions).")
	sample := app.Command("sample", "Show a sample start message for the provided trigger or action.")
	sampleOpt := sample.Arg("handler_name", "Trigger or Action name to generate sample inputs for.").Required().String()
	run := app.Command("run", "Run the plugin (default command). You must supply the start message over STDIN.")
	httpServer := app.Command("http", "Run the plugin as a REST daemon")
	port := app.Flag("port", "The http port to run the server on (defaults to 10001).").Default(DefaultPort).Int()

	args := os.Args[1:] // Chop off the first element, we don't care about the binary name/path

	// Code lifted from old SDK to make kingpin happy
	for i, argv := range args {
		if argv == "--" {
			args = args[0:(i)]
			break
		}
	}
	if len(args) < 1 || (len(args) == 1 && strings.HasSuffix(args[0], "debug")) {
		args = append(args, "run")
	}
	// End of kingpin happiness making

	// Trap the interrupts
	stopChan := make(chan os.Signal, 1)
	signal.Notify(stopChan, syscall.SIGTERM, syscall.SIGINT)
	// Create a context, which will be used to cancel things like triggers in the event of a signal
	ctx, cancel := context.WithCancel(context.Background())
	// Kick off a goroutine to handle the signals and the cancellation
	go cli.HandleShutdown(cancel, stopChan)
	// Invoke the command

	mode := "run"
	cmd, err := app.Parse(args)
	switch kingpin.MustParse(cmd, err) {
	case sample.FullCommand():
		printSampleInput(*sampleOpt)
	case info.FullCommand():
		printInfo()
	case httpServer.FullCommand():
		s, err := http.NewServer(*port, connection.NewCache())
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("Plugin timers booting HTTP Daemon on port %d...", *port)
		// This will block until the server shuts down
		if err := s.ListenAndServe(); err != nil {
			log.Fatal(err)
		}
	case test.FullCommand():
		mode = "test"
		fallthrough
	case run.FullCommand():
		fallthrough
	default:
		// We're running either an action, or a trigger
		m, b, err := getMessageFromStdin()
		if err != nil {
			log.Fatalf("you must provide a message body via STDIN to run an action or trigger: %s", err.Error())
		}
		switch m.Type {
		case message.ActionStart:
			if err := runOneOffAction(mode, b, *debug); err != nil { // Command should be run, or test
				log.Fatal(err)
			}
		case message.TriggerStart:
			// This will block until the trigger shuts down
			if err := runTriggerDaemon(ctx, mode, b, *debug); err != nil { // Command should be run, or test
				log.Fatal(err)
			}
		default:
			log.Fatalf("unknown message type %s", m.Type)
		}
	}
}

func runOneOffAction(mode string, b *message.BodyV1, isDebug bool) error {
	// Set up all the standard data structures we need to process an action
	cd := &connection.Data{}
	l := plog.NewBufferedLogger(plog.Error)
	if mode == "test" || isDebug {
		l.SetLevel(plog.Info)
	}
	// Actions always default to using STDOUT since we never send dispatch info
	// with their message invocations, but to try and keep things consistent between actions
	// and triggers in the hopes of further generalizing their code, we'll continue
	// to use the method below to make the determination of what to use
	d, err := cli.DispatcherFromRaw(b.Dispatcher, isDebug, mode)
	if err != nil {
		return err
	}
	// Make sure we flush the log out stderr as thats how the engine knows to get it in a one off
	defer l.Flush(os.Stderr)
	response := &message.Response{
		Meta:   []byte(`{}`),
		Status: "ok",
	}
	if err = json.Unmarshal(b.Connection, cd); err != nil {
		return err
	}
	var conn *connection.Connection
	conn, err = connection.Connect(cd, l)
	if err != nil {
		return err
	}
	// Unmarshal the body into the right struct
	// We could avoid the 2 excess json marshal calls in here with a lot of switch-casing on types
	// but in this case, the performance gain is not that great, and it's less generator code to maintain
	// to do it this way.
	// TODO if we suspect this is a bottleneck, profile it and swap back to the switch-case approach
	switch b.Action {
	case "delay":
		input := &actions.DelayInput{}
		if err = json.Unmarshal(b.Input, input); err != nil {
			return err
		}
		for _, err = range input.Validate(l) {
			log.Println(fmt.Sprintf("Error while validating DelayTriggerInput: %s", err.Error()))
		}
		if err != nil {
			return fmt.Errorf("Error while validating DelayTriggerInput. Check logs for details")
		}
		a := &actions.DelayAction{}
		runMethod := a.Run
		if mode == "test" {
			runMethod = a.Test
		}
		response.Output, err = runMethod(conn, input, l)
	default:
		return fmt.Errorf("unknown action %s", b.Action)
	}
	if err != nil {
		response.Status = "error"
		response.Error = err.Error()
	}
	response.Log = l.String()
	// dispatch the result
	wrapper := &message.V1{
		Body:    response,
		Type:    "action_event",
		Version: "v1",
	}
	d.Send(wrapper)
	return nil
}

func runTriggerDaemon(ctx context.Context, mode string, b *message.BodyV1, isDebug bool) error {
	// Make a logger
	l := plog.NewNormalLogger(plog.Error)
	if mode == "test" || isDebug {
		l.SetLevel(plog.Info)
	}
	// Serialize the connection data into the raw struct
	cd := &connection.Data{}
	if err := json.Unmarshal(b.Connection, cd); err != nil {
		return err
	}
	// Now, establish a valid connection
	conn, err := connection.Connect(cd, l)
	if err != nil {
		return err
	}
	// Get the dispatcher - will send the messages be sent over stdout or posted over http
	d, err := cli.DispatcherFromRaw(b.Dispatcher, isDebug, mode)
	if err != nil {
		return err
	}
	switch b.Trigger {
	case "daily":
		// Make the input and serialize it into the struct
		input := &triggers.DailyTriggerInput{}
		if err := json.Unmarshal(b.Input, input); err != nil {
			return err
		}
		// Build the trigger
		t := triggers.NewDailyTrigger(d, b.Meta)
		if mode == "test" { // Test mode, use the test method
			// Since the test method doesn't need a run or read loop
			// we do the boring work of packaging the result here
			// Invoke the test, pass the results to the message helper func
			// then pass that message into the dispatcher
			o, err := t.Test(conn, input, l)
			d.Send(cli.WrapTriggerTestResult(l, o, err))
			return nil
		}
		// Start the read loop
		go t.ReadLoop(ctx, l)
		var ti interface{} = t
		if cl, ok := ti.(triggers.DailyTriggerCustomLooper); ok {
			return cl.RunLoopCustom(ctx, conn, input, l)
		}
		// Run will block until it completes / shutsdown
		return t.RunLoop(ctx, conn, input, l)
	case "hourly":
		// Make the input and serialize it into the struct
		input := &triggers.HourlyTriggerInput{}
		if err := json.Unmarshal(b.Input, input); err != nil {
			return err
		}
		// Build the trigger
		t := triggers.NewHourlyTrigger(d, b.Meta)
		if mode == "test" { // Test mode, use the test method
			// Since the test method doesn't need a run or read loop
			// we do the boring work of packaging the result here
			// Invoke the test, pass the results to the message helper func
			// then pass that message into the dispatcher
			o, err := t.Test(conn, input, l)
			d.Send(cli.WrapTriggerTestResult(l, o, err))
			return nil
		}
		// Start the read loop
		go t.ReadLoop(ctx, l)
		var ti interface{} = t
		if cl, ok := ti.(triggers.HourlyTriggerCustomLooper); ok {
			return cl.RunLoopCustom(ctx, conn, input, l)
		}
		// Run will block until it completes / shutsdown
		return t.RunLoop(ctx, conn, input, l)
	case "monthly":
		// Make the input and serialize it into the struct
		input := &triggers.MonthlyTriggerInput{}
		if err := json.Unmarshal(b.Input, input); err != nil {
			return err
		}
		// Build the trigger
		t := triggers.NewMonthlyTrigger(d, b.Meta)
		if mode == "test" { // Test mode, use the test method
			// Since the test method doesn't need a run or read loop
			// we do the boring work of packaging the result here
			// Invoke the test, pass the results to the message helper func
			// then pass that message into the dispatcher
			o, err := t.Test(conn, input, l)
			d.Send(cli.WrapTriggerTestResult(l, o, err))
			return nil
		}
		// Start the read loop
		go t.ReadLoop(ctx, l)
		var ti interface{} = t
		if cl, ok := ti.(triggers.MonthlyTriggerCustomLooper); ok {
			return cl.RunLoopCustom(ctx, conn, input, l)
		}
		// Run will block until it completes / shutsdown
		return t.RunLoop(ctx, conn, input, l)
	case "periodic":
		// Make the input and serialize it into the struct
		input := &triggers.PeriodicTriggerInput{}
		if err := json.Unmarshal(b.Input, input); err != nil {
			return err
		}
		// Build the trigger
		t := triggers.NewPeriodicTrigger(d, b.Meta)
		if mode == "test" { // Test mode, use the test method
			// Since the test method doesn't need a run or read loop
			// we do the boring work of packaging the result here
			// Invoke the test, pass the results to the message helper func
			// then pass that message into the dispatcher
			o, err := t.Test(conn, input, l)
			d.Send(cli.WrapTriggerTestResult(l, o, err))
			return nil
		}
		// Start the read loop
		go t.ReadLoop(ctx, l)
		var ti interface{} = t
		if cl, ok := ti.(triggers.PeriodicTriggerCustomLooper); ok {
			return cl.RunLoopCustom(ctx, conn, input, l)
		}
		// Run will block until it completes / shutsdown
		return t.RunLoop(ctx, conn, input, l)
	case "weekly":
		// Make the input and serialize it into the struct
		input := &triggers.WeeklyTriggerInput{}
		if err := json.Unmarshal(b.Input, input); err != nil {
			return err
		}
		// Build the trigger
		t := triggers.NewWeeklyTrigger(d, b.Meta)
		if mode == "test" { // Test mode, use the test method
			// Since the test method doesn't need a run or read loop
			// we do the boring work of packaging the result here
			// Invoke the test, pass the results to the message helper func
			// then pass that message into the dispatcher
			o, err := t.Test(conn, input, l)
			d.Send(cli.WrapTriggerTestResult(l, o, err))
			return nil
		}
		// Start the read loop
		go t.ReadLoop(ctx, l)
		var ti interface{} = t
		if cl, ok := ti.(triggers.WeeklyTriggerCustomLooper); ok {
			return cl.RunLoopCustom(ctx, conn, input, l)
		}
		// Run will block until it completes / shutsdown
		return t.RunLoop(ctx, conn, input, l)
	default:
		return fmt.Errorf("unknown trigger %s", b.Trigger)
	}
}

func printInfo() {
	// General Info / Header
	result := "\n"
	result += fmt.Sprintf("Name:        %s%s%s\n", cli.Green, Name, cli.Reset)
	result += fmt.Sprintf("Vendor:      %s%s%s\n", cli.Green, Vendor, cli.Reset)
	result += fmt.Sprintf("Version:     %s%s%s\n", cli.Green, Version, cli.Reset)
	result += fmt.Sprintf("Description: %s%s%s\n", cli.Green, Description, cli.Reset)

	// Trigger Info
	result += fmt.Sprintf("\n")
	result += fmt.Sprintf("Triggers (%s%d%s): \n", cli.Green, 5, cli.Reset)
	result += fmt.Sprintf("└── %s%s%s (%s%s)\n", cli.Green, "daily", cli.Reset, "Trigger events daily", cli.Reset)
	result += fmt.Sprintf("└── %s%s%s (%s%s)\n", cli.Green, "hourly", cli.Reset, "Trigger events hourly", cli.Reset)
	result += fmt.Sprintf("└── %s%s%s (%s%s)\n", cli.Green, "monthly", cli.Reset, "Trigger events monthly", cli.Reset)
	result += fmt.Sprintf("└── %s%s%s (%s%s)\n", cli.Green, "periodic", cli.Reset, "Trigger an event periodically", cli.Reset)
	result += fmt.Sprintf("└── %s%s%s (%s%s)\n", cli.Green, "weekly", cli.Reset, "Trigger events weekly", cli.Reset)

	// Action Info
	result += fmt.Sprintf("\n")
	result += fmt.Sprintf("Actions (%s%d%s): \n", cli.Green, 1, cli.Reset)
	result += fmt.Sprintf("└── %s%s%s (%s%s)\n", cli.Green, "delay", cli.Reset, "Delays the workflow by a variable number of seconds", cli.Reset)

	fmt.Print(result)
}

func printSampleInput(action string) error {
	connBytes, err := json.Marshal(connection.Data{})
	if err != nil {
		return err
	}
	b := &message.BodyV1{
		Action:     action,
		Connection: connBytes,
		Meta:       []byte(`{}`),
		Dispatcher: []byte(`{}`),
	}
	m := message.V1{
		Version: "v1",
		Body:    b,
	}
	switch action {
	case "delay":
		m.Type = "action_start"
		actionBytes, err := json.Marshal(actions.DelayInput{})
		if err != nil {
			return err
		}
		b.Input = actionBytes
	case "daily":
		m.Type = "trigger_start"
		triggerBytes, err := json.Marshal(triggers.DailyTriggerInput{})
		if err != nil {
			return err
		}
		b.Input = triggerBytes
	case "hourly":
		m.Type = "trigger_start"
		triggerBytes, err := json.Marshal(triggers.HourlyTriggerInput{})
		if err != nil {
			return err
		}
		b.Input = triggerBytes
	case "monthly":
		m.Type = "trigger_start"
		triggerBytes, err := json.Marshal(triggers.MonthlyTriggerInput{})
		if err != nil {
			return err
		}
		b.Input = triggerBytes
	case "periodic":
		m.Type = "trigger_start"
		triggerBytes, err := json.Marshal(triggers.PeriodicTriggerInput{})
		if err != nil {
			return err
		}
		b.Input = triggerBytes
	case "weekly":
		m.Type = "trigger_start"
		triggerBytes, err := json.Marshal(triggers.WeeklyTriggerInput{})
		if err != nil {
			return err
		}
		b.Input = triggerBytes
	default:
		log.Fatalf("Unknown action or trigger %s", action)
	}

	result, err := json.MarshalIndent(&m, " ", "  ")
	if err != nil {
		return err
	}
	fmt.Println(string(result))
	return nil
}