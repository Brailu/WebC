"""
lightsail.py

Create a container service in lightsail.
"""


import boto3


client = boto3.client("lightsail")

print("creating container service...")

response = client.create_container_service(
    serviceName="webc",
    power="nano",
    scale=1
)

print("DONE")
