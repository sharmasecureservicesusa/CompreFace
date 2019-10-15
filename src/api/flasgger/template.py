template = {
    "swagger": "2.0",
    "info": {
        "description": "Service for face recognition. Upload images with faces of known people, then upload a "
                       "new image, and the service will recognize faces in it. All operations are applied only "
                       "for faces associated with the specified API key.",
        "version": "0.1-snapshot",
        "title": "Exadel Face Recognition Service"
    },
    "host": "msqv355.exadel.by:5001",
    "tags": [
        {
            "name": "Face Database",
        },
        {
            "name": "Face Recognition Model",
        },
        {
            "name": "Maintenance",
        }
    ],
    "schemes": [
        "http"
    ],
    "securityDefinitions": {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-Api-Key"
        }
    },
    "components": {
        "parameters": {
            "RetrainParameter": {
                "name": "retrain",
                "in": "query",
                "description": "Specify whether the model should start retraining immediately after the request is "
                               "completed (set this to False, if operating with a lot of images one after another).",
                "required": "false",
                "type": "string",
                "default": "true"
            },
            "FaceNameParameter": {
                "name": "face_name",
                "in": "path",
                "description": "Person's name to whom the face belongs to.",
                "required": "false",
                "type": "string"
            },
        },
        "responses": {
            "BadRequestResponse": {
                "description": "Bad request is provided",
                "schema": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "example": "Detailed information about the error"
                        }
                    }
                }
            },
            "AccessUnauthorizedResponse": {
                "description": "Given API Key is not authorized",
                "schema": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "example": "Given API Key is not authorized"
                        }
                    }
                }
            },
            "InternalServerErrorResponse": {
                "description": "Internal error has occurred",
                "schema": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "example": "Detailed information about the error"
                        }
                    }
                }
            }
        }
    },
    "externalDocs": {
        "description": "More documentation is available in Confluence",
        "url": "https://confluence.exadel.com/display/KC/Exadel+Face+Recognition+Service"
    }
}
