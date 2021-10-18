# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Check if an IP address is in an address group"


class Input:
    ADDRESS = "address"
    ENABLE_SEARCH = "enable_search"
    GROUP = "group"
    IPV6_GROUP = "ipv6_group"
    

class Output:
    ADDRESS_OBJECTS = "address_objects"
    FOUND = "found"
    

class CheckIfAddressInGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "The Address Object name to check. If Enable Search is set to true then we search the addresses (IP, CIDR, domain) within the address object instead of matching the name",
      "order": 3
    },
    "enable_search": {
      "type": "boolean",
      "title": "Enable Search",
      "description": "When enabled, the Address input will accept a IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don't know the Address Object by its name",
      "default": false,
      "order": 4
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Name of Address Group to check for address",
      "order": 1
    },
    "ipv6_group": {
      "type": "string",
      "title": "IPv6 Group",
      "description": "The name of the IPv6 address group",
      "order": 2
    }
  },
  "required": [
    "address",
    "enable_search",
    "group",
    "ipv6_group"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckIfAddressInGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_objects": {
      "type": "array",
      "title": "Address Objects",
      "description": "The names of the address objects that match or contain the address",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Was address found in group",
      "order": 1
    }
  },
  "required": [
    "address_objects",
    "found"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
