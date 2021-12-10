"""
deploy.py

Creates a container service deployment in lightsail.
"""


import os
import boto3


client = boto3.client("lightsail")

print("creating container service deployment...")

response = client.create_container_service_deployment(
    serviceName="webc",
    containers={
        "webc": {
            "image": "brunitto/webc:latest",
            "environment": {
                "DJANGO_SETTINGS_MODULE": os.environ["DJANGO_SETTINGS_MODULE"],
                "SECRET_KEY": os.environ["SECRET_KEY"]
            },
            "ports": {
                "8000": "HTTP"
            }
        }
    },
    publicEndpoint={
        "containerName": "webc",
        "containerPort": 8000,
        "healthCheck": {
            "path": "/"
        }
    }
)

print("DONE")
