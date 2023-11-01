import json

import requests


def Encode(data: str):
    """Calls the base64 API with a string payload and returns the response."""

    url = "https://base64-api.base64.gke.tanzu.dk/encode"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"data": data})

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception(f"Error calling base64 API: {response.status_code}")

    json_data = json.loads(response.content)

    return json_data["data"]


def Decode(data: str):
    """Calls the base64 API with a string payload and returns the response."""

    url = "https://base64-api.base64.gke.tanzu.dk/decode"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"data": data})

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception(f"Error calling base64 API: {response.status_code}")

    json_data = json.loads(response.content)

    return json_data["data"]
