# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    DOMAIN = "domain"
    HOST = "host"
    USERNAME_AND_PASSWORD = "username_and_password"
    VERIFY_SSL = "verify_ssl"
    

class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "The domian of the user loggin in",
      "order": 2
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "URL to service",
      "order": 3
    },
    "username_and_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Your username and password",
      "order": 1
    },
    "verify_ssl": {
      "type": "boolean",
      "title": "Verify SSL",
      "description": "Enforce signed certificates for the tanium server",
      "order": 4
    }
  },
  "required": [
    "domain",
    "host",
    "username_and_password",
    "verify_ssl"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
