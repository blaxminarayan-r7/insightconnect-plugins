# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a file in a folder"


class Input:
    FILE = "file"
    FOLDER_ID = "folder_id"
    

class Output:
    FILE_ID = "file_id"
    

class CreateFileInFolderInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "$ref": "#/definitions/file",
      "title": "File",
      "description": "The file to create",
      "order": 2
    },
    "folder_id": {
      "type": "string",
      "title": "Folder ID",
      "description": "The ID of the folder where the file will be created",
      "order": 1
    }
  },
  "required": [
    "file",
    "folder_id"
  ],
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateFileInFolderOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file_id": {
      "type": "string",
      "title": "File ID",
      "description": "Return the ID of the file created on Google Drive",
      "order": 1
    }
  },
  "required": [
    "file_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
