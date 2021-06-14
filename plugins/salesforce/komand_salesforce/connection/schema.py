# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    SALESFORCE_ACCOUNT_USERNAME_AND_PASSWORD = "salesforce_account_username_and_password"
    SECURITY_TOKEN = "security_token"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "client_id": {
      "type": "string",
      "title": "Client ID",
      "description": "'Consumer Key' of the connected app",
      "order": 1
    },
    "client_secret": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Client Secret",
      "description": "'Consumer Secret' of the connected app",
      "order": 2
    },
    "salesforce_account_username_and_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Salesforce Account Username and Password",
      "description": "Name and password of the Salesforce user",
      "order": 3
    },
    "security_token": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Security Token",
      "description": "Security token of the Salesforce user",
      "order": 4
    }
  },
  "required": [
    "client_id",
    "client_secret",
    "salesforce_account_username_and_password",
    "security_token"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    },
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
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
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