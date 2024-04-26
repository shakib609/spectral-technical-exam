from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from google.protobuf.json_format import MessageToDict
import grpc

from meterusage_pb2 import MeterUsageRequest
from meterusage_pb2_grpc import MeterUsageStub
from settings import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
)
app.add_middleware(GZipMiddleware)


@app.get("/api/v1/meterusage/")
def get_meterusage_data():
    grpc_channel = grpc.insecure_channel(
        f"{settings.GRPC_SERVER_HOST}:{settings.GRPC_SERVER_PORT}"
    )
    stub = MeterUsageStub(grpc_channel)

    grpc_request = MeterUsageRequest()
    grpc_response = stub.GetMeterUsage(grpc_request)

    response_dict = MessageToDict(grpc_response)
    response_data = response_dict.get("data")
    return response_data
