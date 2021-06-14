# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Read contents from a PCAP file"


class Input:
    FILTER = "filter"
    OPTIONS = "options"
    PCAP = "pcap"
    

class Output:
    DUMP_CONTENTS = "dump_contents"
    DUMP_FILE = "dump_file"
    STDERR = "stderr"
    

class ReadInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "string",
      "title": "BPF",
      "description": "Berkeley Packet Filter E.g. TCP and port 22",
      "order": 3
    },
    "options": {
      "type": "string",
      "title": "Options",
      "description": "Tcpdump Flags and Options E.g. -n -c 10 -s 96. -r is implied",
      "order": 2
    },
    "pcap": {
      "type": "string",
      "title": "PCAP File",
      "displayType": "bytes",
      "description": "Base64 encoded PCAP file",
      "format": "bytes",
      "order": 1
    }
  },
  "required": [
    "pcap"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReadOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "dump_contents": {
      "type": "array",
      "title": "Dump Contents",
      "description": "Traffic Dump as Array",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "dump_file": {
      "type": "string",
      "title": "Dump File",
      "displayType": "bytes",
      "description": "Traffic Dump as File",
      "format": "bytes",
      "order": 2
    },
    "stderr": {
      "type": "string",
      "title": "Standard Error",
      "description": "Tcpdump Standard Error",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)