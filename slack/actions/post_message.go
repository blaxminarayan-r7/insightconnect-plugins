package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// PostMessageInput is the input for PostMessage
type PostMessageInput struct {
	Attachments []interface{} `json:"attachments"`
	Channel     string        `json:"channel"`
	ChannelID   string        `json:"channel_id"`
	IconEmoji   string        `json:"icon_emoji"`
	Message     string        `json:"message"`
	Username    string        `json:"username"`
}

// PostMessageOutput is the output for PostMessage
type PostMessageOutput struct {
	MessageID string `json:"message_id"`
	Timestamp string `json:"timestamp"`
}

// PostMessageAction is an action the plugin can take
type PostMessageAction struct{}