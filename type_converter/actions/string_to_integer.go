package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// StringToIntegerInput is the input for StringToInteger
type StringToIntegerInput struct {
	Input string `json:"input"`
	Strip bool   `json:"strip"`
}

// StringToIntegerOutput is the output for StringToInteger
type StringToIntegerOutput struct {
	Output int `json:"output"`
}

// StringToIntegerAction is an action the plugin can take
type StringToIntegerAction struct{}