from fastapi.testclient import TestClient
from unittest.mock import patch
from google.protobuf.timestamp_pb2 import Timestamp

from main import app
from meterusage_pb2 import MeterUsageResponse, MeterUsageData
from utils import convert_timestamp_to_iso

client = TestClient(app)


@patch("main.MeterUsageStub")
def test_get_meterusage_data(mock_stub):
    page_number = 1
    page_size = 5
    total_pages = 1

    test_meterusage_data = [
        MeterUsageData(time=Timestamp(seconds=1629142443), meterusage=12.5),
        MeterUsageData(time=Timestamp(seconds=1629199999), meterusage=12.5),
    ]

    # Arrange
    mock_response = MeterUsageResponse()
    mock_response.data.extend(test_meterusage_data)
    mock_response.page_number = page_number
    mock_response.page_size = page_size
    mock_response.total_pages = total_pages
    mock_stub.return_value.GetMeterUsage.return_value = mock_response

    response = client.get(
        "/api/v1/meterusage/",
        params={
            "page_number": page_number,
            "page_size": page_size,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {
                "time": convert_timestamp_to_iso(test_data.time.seconds),
                "meterusage": test_data.meterusage,
            }
            for test_data in test_meterusage_data
        ],
        "pageNumber": page_number,
        "pageSize": page_size,
        "totalPages": total_pages,
    }
