# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get query results for a LEQL query by query ID"


class Input:
    ID = "id"
    

class Output:
    EVENTS = "events"
    

class QueryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Log ID",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QueryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "events": {
      "type": "array",
      "title": "Events",
      "description": "Events from logs",
      "items": {
        "$ref": "#/definitions/events"
      },
      "order": 1
    }
  },
  "required": [
    "events"
  ],
  "definitions": {
    "eventData": {
      "type": "object",
      "title": "eventData",
      "properties": {
        "asSignatureCreationTime": {
          "type": "string",
          "title": "As Signature Creation Time",
          "description": "As signature creation time",
          "order": 6
        },
        "assignatureVersion": {
          "type": "string",
          "title": "As Signature Version",
          "description": "As signature version",
          "order": 4
        },
        "avSignatureCreationTime": {
          "type": "string",
          "title": "AV Signature Creation Time",
          "description": "AV signature creation time",
          "order": 20
        },
        "avsignatureVersion": {
          "type": "string",
          "title": "AV Signature Version",
          "description": "AV signature version",
          "order": 21
        },
        "bmState": {
          "type": "string",
          "title": "BMS State",
          "description": "BMS state",
          "order": 11
        },
        "data": {
          "type": "array",
          "title": "Data",
          "description": "Data",
          "items": {
            "type": "object"
          },
          "order": 18
        },
        "engineVersion": {
          "type": "string",
          "title": "Engine Version",
          "description": "Engine version",
          "order": 10
        },
        "ioavState": {
          "type": "string",
          "title": "IOAV State",
          "description": "IOAV state",
          "order": 5
        },
        "lastAsSignatureAge": {
          "type": "string",
          "title": "Last As Signature Age",
          "description": "Last as signature age",
          "order": 2
        },
        "lastAvSignatureAge": {
          "type": "string",
          "title": "Last AV Signature Age",
          "description": "Last AV signature age",
          "order": 22
        },
        "lastFullScanAge": {
          "type": "string",
          "title": "Last Full Scan Age",
          "description": "Last full scan age",
          "order": 25
        },
        "lastFullScanEndTime": {
          "type": "string",
          "title": "Last Full Scan End Time",
          "description": "Last full scan end time",
          "order": 13
        },
        "lastFullScanSource": {
          "type": "string",
          "title": "Last Full Scan Source",
          "description": "Last full scan source",
          "order": 7
        },
        "lastFullScanStartTime": {
          "type": "string",
          "title": "Last Full Scan Start Time",
          "description": "Last full scan start time",
          "order": 9
        },
        "lastQuickScanAge": {
          "type": "string",
          "title": "Last Quick Scan Age",
          "description": "Last quick scan age",
          "order": 17
        },
        "lastQuickScanEndTime": {
          "type": "string",
          "title": "Last Quick Scan End Time",
          "description": "Last quick scan end time",
          "order": 19
        },
        "lastQuickScanSource": {
          "type": "string",
          "title": "Last Quick Scan Source",
          "description": "Last quick scan source",
          "order": 12
        },
        "lastQuickScanStartTime": {
          "type": "string",
          "title": "Last Quick Scan Start Time",
          "description": "Last quick scan start time",
          "order": 24
        },
        "nriEngineVersion": {
          "type": "string",
          "title": "NRI Engine Version",
          "description": "NRI engine version",
          "order": 23
        },
        "nriSignatureVersion": {
          "type": "string",
          "title": "NRI Signature Version",
          "description": "NRI signature version",
          "order": 8
        },
        "oaState": {
          "type": "string",
          "title": "OA State",
          "description": "OA state",
          "order": 1
        },
        "platformVersion": {
          "type": "string",
          "title": "Platform Version",
          "description": "Platform version",
          "order": 16
        },
        "productName": {
          "type": "string",
          "title": "Product Name",
          "description": "Product name",
          "order": 14
        },
        "productStatus": {
          "type": "string",
          "title": "Product Status",
          "description": "Product status",
          "order": 3
        },
        "rtpState": {
          "type": "string",
          "title": "RTP State",
          "description": "RTP state",
          "order": 15
        }
      }
    },
    "events": {
      "type": "object",
      "title": "events",
      "properties": {
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "List of labels",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Links",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 6
        },
        "log_id": {
          "type": "string",
          "title": "Log ID",
          "description": "Log ID",
          "order": 4
        },
        "message": {
          "$ref": "#/definitions/message",
          "title": "Message",
          "description": "Message",
          "order": 5
        },
        "sequence_number": {
          "type": "integer",
          "title": "Sequence Number",
          "description": "Sequence number",
          "order": 3
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "Timestamp",
          "order": 2
        }
      },
      "definitions": {
        "eventData": {
          "type": "object",
          "title": "eventData",
          "properties": {
            "asSignatureCreationTime": {
              "type": "string",
              "title": "As Signature Creation Time",
              "description": "As signature creation time",
              "order": 6
            },
            "assignatureVersion": {
              "type": "string",
              "title": "As Signature Version",
              "description": "As signature version",
              "order": 4
            },
            "avSignatureCreationTime": {
              "type": "string",
              "title": "AV Signature Creation Time",
              "description": "AV signature creation time",
              "order": 20
            },
            "avsignatureVersion": {
              "type": "string",
              "title": "AV Signature Version",
              "description": "AV signature version",
              "order": 21
            },
            "bmState": {
              "type": "string",
              "title": "BMS State",
              "description": "BMS state",
              "order": 11
            },
            "data": {
              "type": "array",
              "title": "Data",
              "description": "Data",
              "items": {
                "type": "object"
              },
              "order": 18
            },
            "engineVersion": {
              "type": "string",
              "title": "Engine Version",
              "description": "Engine version",
              "order": 10
            },
            "ioavState": {
              "type": "string",
              "title": "IOAV State",
              "description": "IOAV state",
              "order": 5
            },
            "lastAsSignatureAge": {
              "type": "string",
              "title": "Last As Signature Age",
              "description": "Last as signature age",
              "order": 2
            },
            "lastAvSignatureAge": {
              "type": "string",
              "title": "Last AV Signature Age",
              "description": "Last AV signature age",
              "order": 22
            },
            "lastFullScanAge": {
              "type": "string",
              "title": "Last Full Scan Age",
              "description": "Last full scan age",
              "order": 25
            },
            "lastFullScanEndTime": {
              "type": "string",
              "title": "Last Full Scan End Time",
              "description": "Last full scan end time",
              "order": 13
            },
            "lastFullScanSource": {
              "type": "string",
              "title": "Last Full Scan Source",
              "description": "Last full scan source",
              "order": 7
            },
            "lastFullScanStartTime": {
              "type": "string",
              "title": "Last Full Scan Start Time",
              "description": "Last full scan start time",
              "order": 9
            },
            "lastQuickScanAge": {
              "type": "string",
              "title": "Last Quick Scan Age",
              "description": "Last quick scan age",
              "order": 17
            },
            "lastQuickScanEndTime": {
              "type": "string",
              "title": "Last Quick Scan End Time",
              "description": "Last quick scan end time",
              "order": 19
            },
            "lastQuickScanSource": {
              "type": "string",
              "title": "Last Quick Scan Source",
              "description": "Last quick scan source",
              "order": 12
            },
            "lastQuickScanStartTime": {
              "type": "string",
              "title": "Last Quick Scan Start Time",
              "description": "Last quick scan start time",
              "order": 24
            },
            "nriEngineVersion": {
              "type": "string",
              "title": "NRI Engine Version",
              "description": "NRI engine version",
              "order": 23
            },
            "nriSignatureVersion": {
              "type": "string",
              "title": "NRI Signature Version",
              "description": "NRI signature version",
              "order": 8
            },
            "oaState": {
              "type": "string",
              "title": "OA State",
              "description": "OA state",
              "order": 1
            },
            "platformVersion": {
              "type": "string",
              "title": "Platform Version",
              "description": "Platform version",
              "order": 16
            },
            "productName": {
              "type": "string",
              "title": "Product Name",
              "description": "Product name",
              "order": 14
            },
            "productStatus": {
              "type": "string",
              "title": "Product Status",
              "description": "Product status",
              "order": 3
            },
            "rtpState": {
              "type": "string",
              "title": "RTP State",
              "description": "RTP state",
              "order": 15
            }
          }
        },
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "HREF",
              "description": "HREF",
              "order": 2
            },
            "rel": {
              "type": "string",
              "title": "Relation",
              "description": "Relation",
              "order": 1
            }
          }
        },
        "message": {
          "type": "object",
          "title": "message",
          "properties": {
            "computerName": {
              "type": "string",
              "title": "Computer Name",
              "order": 3
            },
            "eventCode": {
              "type": "integer",
              "title": "Event Code",
              "order": 2
            },
            "eventData": {
              "$ref": "#/definitions/eventData",
              "title": "Event Data",
              "order": 6
            },
            "isDomainController": {
              "type": "boolean",
              "title": "Is Domain Controller",
              "order": 5
            },
            "sid": {
              "type": "string",
              "title": "SID",
              "order": 4
            },
            "sourceName": {
              "type": "string",
              "title": "Source Name",
              "order": 1
            },
            "timeWritten": {
              "type": "string",
              "title": "Time Written",
              "order": 7
            }
          },
          "definitions": {
            "eventData": {
              "type": "object",
              "title": "eventData",
              "properties": {
                "asSignatureCreationTime": {
                  "type": "string",
                  "title": "As Signature Creation Time",
                  "description": "As signature creation time",
                  "order": 6
                },
                "assignatureVersion": {
                  "type": "string",
                  "title": "As Signature Version",
                  "description": "As signature version",
                  "order": 4
                },
                "avSignatureCreationTime": {
                  "type": "string",
                  "title": "AV Signature Creation Time",
                  "description": "AV signature creation time",
                  "order": 20
                },
                "avsignatureVersion": {
                  "type": "string",
                  "title": "AV Signature Version",
                  "description": "AV signature version",
                  "order": 21
                },
                "bmState": {
                  "type": "string",
                  "title": "BMS State",
                  "description": "BMS state",
                  "order": 11
                },
                "data": {
                  "type": "array",
                  "title": "Data",
                  "description": "Data",
                  "items": {
                    "type": "object"
                  },
                  "order": 18
                },
                "engineVersion": {
                  "type": "string",
                  "title": "Engine Version",
                  "description": "Engine version",
                  "order": 10
                },
                "ioavState": {
                  "type": "string",
                  "title": "IOAV State",
                  "description": "IOAV state",
                  "order": 5
                },
                "lastAsSignatureAge": {
                  "type": "string",
                  "title": "Last As Signature Age",
                  "description": "Last as signature age",
                  "order": 2
                },
                "lastAvSignatureAge": {
                  "type": "string",
                  "title": "Last AV Signature Age",
                  "description": "Last AV signature age",
                  "order": 22
                },
                "lastFullScanAge": {
                  "type": "string",
                  "title": "Last Full Scan Age",
                  "description": "Last full scan age",
                  "order": 25
                },
                "lastFullScanEndTime": {
                  "type": "string",
                  "title": "Last Full Scan End Time",
                  "description": "Last full scan end time",
                  "order": 13
                },
                "lastFullScanSource": {
                  "type": "string",
                  "title": "Last Full Scan Source",
                  "description": "Last full scan source",
                  "order": 7
                },
                "lastFullScanStartTime": {
                  "type": "string",
                  "title": "Last Full Scan Start Time",
                  "description": "Last full scan start time",
                  "order": 9
                },
                "lastQuickScanAge": {
                  "type": "string",
                  "title": "Last Quick Scan Age",
                  "description": "Last quick scan age",
                  "order": 17
                },
                "lastQuickScanEndTime": {
                  "type": "string",
                  "title": "Last Quick Scan End Time",
                  "description": "Last quick scan end time",
                  "order": 19
                },
                "lastQuickScanSource": {
                  "type": "string",
                  "title": "Last Quick Scan Source",
                  "description": "Last quick scan source",
                  "order": 12
                },
                "lastQuickScanStartTime": {
                  "type": "string",
                  "title": "Last Quick Scan Start Time",
                  "description": "Last quick scan start time",
                  "order": 24
                },
                "nriEngineVersion": {
                  "type": "string",
                  "title": "NRI Engine Version",
                  "description": "NRI engine version",
                  "order": 23
                },
                "nriSignatureVersion": {
                  "type": "string",
                  "title": "NRI Signature Version",
                  "description": "NRI signature version",
                  "order": 8
                },
                "oaState": {
                  "type": "string",
                  "title": "OA State",
                  "description": "OA state",
                  "order": 1
                },
                "platformVersion": {
                  "type": "string",
                  "title": "Platform Version",
                  "description": "Platform version",
                  "order": 16
                },
                "productName": {
                  "type": "string",
                  "title": "Product Name",
                  "description": "Product name",
                  "order": 14
                },
                "productStatus": {
                  "type": "string",
                  "title": "Product Status",
                  "description": "Product status",
                  "order": 3
                },
                "rtpState": {
                  "type": "string",
                  "title": "RTP State",
                  "description": "RTP state",
                  "order": 15
                }
              }
            }
          }
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "HREF",
          "order": 2
        },
        "rel": {
          "type": "string",
          "title": "Relation",
          "description": "Relation",
          "order": 1
        }
      }
    },
    "message": {
      "type": "object",
      "title": "message",
      "properties": {
        "computerName": {
          "type": "string",
          "title": "Computer Name",
          "order": 3
        },
        "eventCode": {
          "type": "integer",
          "title": "Event Code",
          "order": 2
        },
        "eventData": {
          "$ref": "#/definitions/eventData",
          "title": "Event Data",
          "order": 6
        },
        "isDomainController": {
          "type": "boolean",
          "title": "Is Domain Controller",
          "order": 5
        },
        "sid": {
          "type": "string",
          "title": "SID",
          "order": 4
        },
        "sourceName": {
          "type": "string",
          "title": "Source Name",
          "order": 1
        },
        "timeWritten": {
          "type": "string",
          "title": "Time Written",
          "order": 7
        }
      },
      "definitions": {
        "eventData": {
          "type": "object",
          "title": "eventData",
          "properties": {
            "asSignatureCreationTime": {
              "type": "string",
              "title": "As Signature Creation Time",
              "description": "As signature creation time",
              "order": 6
            },
            "assignatureVersion": {
              "type": "string",
              "title": "As Signature Version",
              "description": "As signature version",
              "order": 4
            },
            "avSignatureCreationTime": {
              "type": "string",
              "title": "AV Signature Creation Time",
              "description": "AV signature creation time",
              "order": 20
            },
            "avsignatureVersion": {
              "type": "string",
              "title": "AV Signature Version",
              "description": "AV signature version",
              "order": 21
            },
            "bmState": {
              "type": "string",
              "title": "BMS State",
              "description": "BMS state",
              "order": 11
            },
            "data": {
              "type": "array",
              "title": "Data",
              "description": "Data",
              "items": {
                "type": "object"
              },
              "order": 18
            },
            "engineVersion": {
              "type": "string",
              "title": "Engine Version",
              "description": "Engine version",
              "order": 10
            },
            "ioavState": {
              "type": "string",
              "title": "IOAV State",
              "description": "IOAV state",
              "order": 5
            },
            "lastAsSignatureAge": {
              "type": "string",
              "title": "Last As Signature Age",
              "description": "Last as signature age",
              "order": 2
            },
            "lastAvSignatureAge": {
              "type": "string",
              "title": "Last AV Signature Age",
              "description": "Last AV signature age",
              "order": 22
            },
            "lastFullScanAge": {
              "type": "string",
              "title": "Last Full Scan Age",
              "description": "Last full scan age",
              "order": 25
            },
            "lastFullScanEndTime": {
              "type": "string",
              "title": "Last Full Scan End Time",
              "description": "Last full scan end time",
              "order": 13
            },
            "lastFullScanSource": {
              "type": "string",
              "title": "Last Full Scan Source",
              "description": "Last full scan source",
              "order": 7
            },
            "lastFullScanStartTime": {
              "type": "string",
              "title": "Last Full Scan Start Time",
              "description": "Last full scan start time",
              "order": 9
            },
            "lastQuickScanAge": {
              "type": "string",
              "title": "Last Quick Scan Age",
              "description": "Last quick scan age",
              "order": 17
            },
            "lastQuickScanEndTime": {
              "type": "string",
              "title": "Last Quick Scan End Time",
              "description": "Last quick scan end time",
              "order": 19
            },
            "lastQuickScanSource": {
              "type": "string",
              "title": "Last Quick Scan Source",
              "description": "Last quick scan source",
              "order": 12
            },
            "lastQuickScanStartTime": {
              "type": "string",
              "title": "Last Quick Scan Start Time",
              "description": "Last quick scan start time",
              "order": 24
            },
            "nriEngineVersion": {
              "type": "string",
              "title": "NRI Engine Version",
              "description": "NRI engine version",
              "order": 23
            },
            "nriSignatureVersion": {
              "type": "string",
              "title": "NRI Signature Version",
              "description": "NRI signature version",
              "order": 8
            },
            "oaState": {
              "type": "string",
              "title": "OA State",
              "description": "OA state",
              "order": 1
            },
            "platformVersion": {
              "type": "string",
              "title": "Platform Version",
              "description": "Platform version",
              "order": 16
            },
            "productName": {
              "type": "string",
              "title": "Product Name",
              "description": "Product name",
              "order": 14
            },
            "productStatus": {
              "type": "string",
              "title": "Product Status",
              "description": "Product status",
              "order": 3
            },
            "rtpState": {
              "type": "string",
              "title": "RTP State",
              "description": "RTP state",
              "order": 15
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
