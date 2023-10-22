"""Base64 Encode and decode API"""
import base64

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Hack for TAP to reconize openapi
app.openapi_version = "3.0.0"

origins = [
    "https://tap-gui.gke.tanzu.dk",
    "http://tap-gui.gke.tanzu.dk",
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    """Class defining the data schema"""
    data: str

@app.get("/")
def read_root():
    """Function for test on /"""
    return {"Hello": "World"}

@app.post("/encode/")
def encode_text(data: Data):
    """Function for encoding Base64"""
    dict_data = data.model_dump()
    source_value = dict_data['data']
    source_value = source_value.encode("ascii")
    base64_bytes = base64.b64encode(source_value)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


@app.post("/decode/")
def decode_text(data: Data):
    """Function for decoding Base64"""
    dict_data = data.model_dump()
    source_value = dict_data['data']
    source_value = source_value.encode("ascii")
    base64_bytes = base64.b64decode(source_value)
    base64_string = base64_bytes.decode("ascii")
    return base64_string
