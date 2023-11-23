"""Functions that call the Backend part of the Base64 App"""
import json
import os

import requests


def Encode(data: str):
    """Calls the base64 API with a string payload and returns the response."""
    api_host = os.environ['API_HOST']
    api_port = os.environ['API_PORT']
    url = api_host + ":"+api_port + "/encode"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"data": data})

    response = requests.post(url, headers=headers, data=payload, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Error calling base64 API: {response.status_code}")

    json_data = json.loads(response.content)

    return json_data["data"]


def Decode(data: str):
    """Calls the base64 API with a string payload and returns the response."""
    api_host = os.environ['API_HOST']
    api_port = os.environ['API_PORT']
    url = api_host + ":"+api_port + "/decode"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"data": data})

    response = requests.post(url, headers=headers, data=payload, timeout=10)

    if response.status_code != 200:
        raise Exception(f"Error calling base64 API: {response.status_code}")

    json_data = json.loads(response.content)

    return json_data["data"]
