# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Rename a destination list"


class Input:
    DESTINATIONLISTID = "destinationListId"
    ORGANIZATIONID = "organizationId"
    PAYLOAD = "payload"
    

class Output:
    SUCCESS = "success"
    

class DlPatchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "destinationListId": {
      "type": "integer",
      "title": "Destination List ID",
      "description": "Unique ID for destination list",
      "order": 2
    },
    "organizationId": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Organisation ID",
      "order": 1
    },
    "payload": {
      "type": "array",
      "title": "Payload",
      "description": "value containing name to change to",
      "items": {
        "$ref": "#/definitions/dlPatch"
      },
      "order": 3
    }
  },
  "required": [
    "destinationListId",
    "organizationId"
  ],
  "definitions": {
    "dlPatch": {
      "type": "object",
      "title": "dlPatch",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the destination list",
          "order": 1
        }
      },
      "required": [
        "name"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DlPatchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "array",
      "title": "Success",
      "items": {
        "$ref": "#/definitions/dlEntity"
      },
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "dlEntity": {
      "type": "object",
      "title": "dlEntity",
      "properties": {
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Access can be allow or block. It defines destinationList type, e.g. allow",
          "order": 3
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "example, 1490206249",
          "order": 7
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique id of the destination list.",
          "order": 1
        },
        "isGlobal": {
          "type": "boolean",
          "title": "Is Global",
          "description": "isGlobal can be true or false. There is only one default destination list of type allow or block for an organization.",
          "order": 4
        },
        "isMspDefault": {
          "type": "boolean",
          "title": "Is MSP Default",
          "description": "example, false",
          "order": 9
        },
        "markedForDeletion": {
          "type": "boolean",
          "title": "Marked For Deletion",
          "description": "example, false",
          "order": 10
        },
        "meta": {
          "type": "array",
          "title": "Meta Data",
          "description": "None",
          "items": {
            "$ref": "#/definitions/meta"
          },
          "order": 11
        },
        "modifiedAt": {
          "type": "integer",
          "title": "Modified At",
          "description": "example, 1490206249",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the DL list",
          "order": 5
        },
        "organizationId": {
          "type": "integer",
          "title": "Organization Id",
          "description": "ID of org, e.g. 2345678",
          "order": 2
        },
        "thirdpartyCategoryId": {
          "type": "integer",
          "title": "Third Party Category Id",
          "description": "example, 0",
          "order": 6
        }
      },
      "definitions": {
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "destinationCount": {
              "type": "integer",
              "title": "DestinationCount",
              "description": "Total number of destinations in a destination list.",
              "order": 1
            },
            "domainCount": {
              "type": "integer",
              "title": "DomainCount",
              "description": "Total number of domains in a destination list. Domains are part of total destinations in a destination lists.",
              "order": 2
            },
            "ipv4Count": {
              "type": "integer",
              "title": "Ipv4Count",
              "description": "Total number of Ip's in a destination list. Ip's are part of total destinations in a destination lists.",
              "order": 4
            },
            "urlCount": {
              "type": "integer",
              "title": "UrlCount",
              "description": "Total number of Urls in a destination list. Urls are part of total destinations in a destination lists.",
              "order": 3
            }
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "destinationCount": {
          "type": "integer",
          "title": "DestinationCount",
          "description": "Total number of destinations in a destination list.",
          "order": 1
        },
        "domainCount": {
          "type": "integer",
          "title": "DomainCount",
          "description": "Total number of domains in a destination list. Domains are part of total destinations in a destination lists.",
          "order": 2
        },
        "ipv4Count": {
          "type": "integer",
          "title": "Ipv4Count",
          "description": "Total number of Ip's in a destination list. Ip's are part of total destinations in a destination lists.",
          "order": 4
        },
        "urlCount": {
          "type": "integer",
          "title": "UrlCount",
          "description": "Total number of Urls in a destination list. Urls are part of total destinations in a destination lists.",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
