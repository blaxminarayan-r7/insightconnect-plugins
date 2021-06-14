# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action searches for agents and returns device information details"


class Input:
    AGENT = "agent"


class Output:
    AGENTS = "agents"


class SearchAgentsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to retrieve device information from. Accepts IP address, MAC address, name, or device ID",
      "order": 1
    }
  },
  "required": [
    "agent"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchAgentsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agents": {
      "type": "array",
      "title": "Agents",
      "description": "Detailed information about agents found",
      "items": {
        "$ref": "#/definitions/agents"
      },
      "order": 1
    }
  },
  "required": [
    "agents"
  ],
  "definitions": {
    "agents": {
      "type": "object",
      "title": "agents",
      "properties": {
        "agent_version": {
          "type": "string",
          "title": "Agent Version",
          "description": "Agent version",
          "order": 4
        },
        "date_first_registered": {
          "type": "string",
          "title": "Date First Registered",
          "description": "Date first registered",
          "order": 6
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "ip_addresses": {
          "type": "array",
          "title": "IP Addresses",
          "description": "IP addresses",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "mac_addresses": {
          "type": "array",
          "title": "MAC Addresses",
          "description": "MAC addresses",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "policy": {
          "$ref": "#/definitions/policy",
          "title": "Policy",
          "description": "Policy",
          "order": 5
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 3
        }
      },
      "definitions": {
        "policy": {
          "type": "object",
          "title": "policy",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            }
          }
        }
      }
    },
    "policy": {
      "type": "object",
      "title": "policy",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)