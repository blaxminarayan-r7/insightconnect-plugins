# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search a email for malicious threats"


class Input:
    EMAIL = "email"
    

class Output:
    DOMAINS = "domains"
    FOUND = "found"
    PERMALINK = "permalink"
    REFERENCES = "references"
    

class EmailInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Email",
      "description": "Email to search",
      "order": 1
    }
  },
  "required": [
    "email"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EmailOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domains": {
      "type": "array",
      "title": "Domains",
      "description": "List of domains",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether search returned results",
      "order": 4
    },
    "permalink": {
      "type": "string",
      "title": "Permalink",
      "description": "Permalink URL",
      "order": 3
    },
    "references": {
      "type": "array",
      "title": "References",
      "description": "List of references",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "found"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)