# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve all saved question definitions on the server."


class Input:
    MAXIMUM_RETURNED_QUESTIONS = "maximum_returned_questions"
    

class Output:
    QUESTIONS = "questions"
    

class ListSavedQuestionsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "maximum_returned_questions": {
      "type": "integer",
      "title": "Maximum Returned Questions",
      "description": "The maximum number of questions to return use 0 for unlimited",
      "order": 1
    }
  },
  "required": [
    "maximum_returned_questions"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListSavedQuestionsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "questions": {
      "type": "array",
      "title": "Questions",
      "description": "A list of saved suestions",
      "items": {
        "$ref": "#/definitions/question"
      },
      "order": 1
    }
  },
  "required": [
    "questions"
  ],
  "definitions": {
    "question": {
      "type": "object",
      "title": "question",
      "properties": {
        "action_tracking_flag": {
          "type": "boolean",
          "title": "Action Tracking Flag",
          "description": "Action tracking flag",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
