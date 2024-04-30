from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.json_format import MessageToDict
from unittest.mock import patch, MagicMock
from meterusage_pb2 import MeterUsageData, MeterUsageRequest, MeterUsageResponse
from service import MeterUsageService


@patch("service.Database")
def test_MeterUsageService_GetMeterUsage_with_empty_database(mock_db):
    page_number = 1
    page_size = 5

    mock_db.return_value.get_paginated_data = MagicMock(
        return_value={"data": [], "total_pages": 1}
    )
    service = MeterUsageService()
    request = MeterUsageRequest(page_number=page_number, page_size=page_size)

    response = service.GetMeterUsage(request, None)

    assert isinstance(response, MeterUsageResponse)
    assert response.page_number == page_number
    assert response.page_size == page_size
    assert response.total_pages == 1
    assert len(response.data) == 0


@patch("service.Database")
def test_MeterUsageService_GetMeterUsage_with_database_entries(mock_db):
    page_number = 1
    page_size = 5

    dummy_test_meterusage_data = [
        {"time": Timestamp(seconds=1629142443), "meterusage": 12.5},
        {"time": Timestamp(seconds=1629199999), "meterusage": 99.5},
    ]

    mock_db.return_value.get_paginated_data = MagicMock(
        return_value={
            "data": dummy_test_meterusage_data,
            "total_pages": 1,
        }
    )
    service = MeterUsageService()
    request = MeterUsageRequest(page_number=page_number, page_size=page_size)

    response = service.GetMeterUsage(request, None)

    assert isinstance(response, MeterUsageResponse)
    assert response.page_number == page_number
    assert response.page_size == page_size
    assert response.total_pages == 1
    for i, test_data in enumerate(response.data):
        assert test_data.time == dummy_test_meterusage_data[i]["time"]
        assert test_data.meterusage == dummy_test_meterusage_data[i]["meterusage"]
