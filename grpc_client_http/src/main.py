from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from google.protobuf.json_format import MessageToDict
import grpc

from meterusage_pb2 import MeterUsageRequest
from meterusage_pb2_grpc import MeterUsageStub
from models import MeterUsageResponseModel
from settings import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
)
app.add_middleware(GZipMiddleware)

grpc_channel = grpc.insecure_channel(
    f"{settings.GRPC_SERVER_HOST}:{settings.GRPC_SERVER_PORT}",
    options=[
        ("grpc.keepalive_time_ms", 30000),  # Send keepalive ping every 30 seconds
        ("grpc.keepalive_timeout_ms", 5000),  # Timeout for keepalive ping is 5 seconds
        (
            "grpc.keepalive_permit_without_calls",
            True,
        ),  # Allow keepalive pings without calls
        (
            "grpc.http2.max_pings_without_data",
            0,
        ),  # Allow unlimited keepalive pings without data
        (
            "grpc.http2.min_time_between_pings_ms",
            10000,
        ),  # Minimum time between pings is 10 seconds
    ],
    compression=grpc.Compression.Gzip,
)


@app.get(
    "/api/v1/meterusage/",
    summary="Get meter usage data",
    description="This API returns paginated meter usage data from a gRPC service.",
    response_description="A JSON object containing the meter usage data",
    response_model=MeterUsageResponseModel,
    response_class=ORJSONResponse,
)
def get_meterusage_data(
    page_number: int = Query(1, description="The page number to fetch. Defaults to 1."),
    page_size: int = Query(
        100, description="The number of items per page. Defaults to 100."
    ),
):
    stub = MeterUsageStub(grpc_channel)
    grpc_request = MeterUsageRequest(page_number=page_number, page_size=page_size)
    grpc_response = stub.GetMeterUsage(grpc_request)
    response_data = MessageToDict(grpc_response)
    return response_data
