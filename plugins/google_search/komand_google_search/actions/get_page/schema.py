# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Request the given URL and return the response page, using the cookie jar"


class Input:
    URL = "url"
    

class Output:
    WEB_PAGE = "web_page"
    

class GetPageInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to retrieve e.g. https://www.google.com",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPageOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "web_page": {
      "type": "string",
      "title": "Web Page",
      "description": "Web page",
      "order": 1
    }
  },
  "required": [
    "web_page"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)