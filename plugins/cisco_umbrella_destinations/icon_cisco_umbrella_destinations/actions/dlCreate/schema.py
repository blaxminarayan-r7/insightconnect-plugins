# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a destination list"


class Input:
    ORGANIZATIONID = "organizationId"
    PAYLOAD = "payload"
    

class Output:
    SUCCESS = "success"
    

class DlCreateInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organizationId": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Organisation ID",
      "order": 1
    },
    "payload": {
      "type": "array",
      "title": "Payload",
      "description": "List of destinations",
      "items": {
        "$ref": "#/definitions/dlCreate"
      },
      "order": 2
    }
  },
  "required": [
    "organizationId",
    "payload"
  ],
  "definitions": {
    "destinations": {
      "type": "object",
      "title": "destinations",
      "properties": {
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "e.g. Added new destination list",
          "order": 3
        },
        "destination": {
          "type": "string",
          "title": "Destination",
          "description": "Destination can be domain, url or ip | e.g. \\u003cdomain_name\\u003e",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type can be DOMAIN, URL, IPV4 | e.g. DOMAIN",
          "order": 2
        }
      },
      "required": [
        "destination",
        "type"
      ]
    },
    "dlCreate": {
      "type": "object",
      "title": "dlCreate",
      "properties": {
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Access can be allow or block. It defines destinationlist type.",
          "order": 1
        },
        "destinations": {
          "type": "array",
          "title": "Destinations",
          "description": "Destinations to add to new list",
          "items": {
            "$ref": "#/definitions/destinations"
          },
          "order": 4
        },
        "isGlobal": {
          "type": "boolean",
          "title": "IsGlobal",
          "description": "isGlobal can be true or false. There is only one default destination list of type allow or block for an organization.",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "example, New Destination List",
          "order": 3
        }
      },
      "required": [
        "access",
        "isGlobal",
        "name"
      ],
      "definitions": {
        "destinations": {
          "type": "object",
          "title": "destinations",
          "properties": {
            "comment": {
              "type": "string",
              "title": "Comment",
              "description": "e.g. Added new destination list",
              "order": 3
            },
            "destination": {
              "type": "string",
              "title": "Destination",
              "description": "Destination can be domain, url or ip | e.g. \\u003cdomain_name\\u003e",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type can be DOMAIN, URL, IPV4 | e.g. DOMAIN",
              "order": 2
            }
          },
          "required": [
            "destination",
            "type"
          ]
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DlCreateOutput(insightconnect_plugin_runtime.Output):
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