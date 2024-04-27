from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
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
    f"{settings.GRPC_SERVER_HOST}:{settings.GRPC_SERVER_PORT}"
)


@app.get(
    "/api/v1/meterusage/",
    summary="Get meter usage data",
    description="This API returns paginated meter usage data from a gRPC service.",
    response_description="A JSON object containing the meter usage data",
    response_model=MeterUsageResponseModel,
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
