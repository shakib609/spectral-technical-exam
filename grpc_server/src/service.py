from database import Database
from meterusage_pb2 import MeterUsageRequest, MeterUsageResponse
from meterusage_pb2_grpc import MeterUsageServicer

METERUSAGE_CSV_FILE = "meterusage.csv"


class MeterUsageService(MeterUsageServicer):

    def __init__(self):
        super().__init__()
        self.database = Database()
        self.database.load_data_from_csv_file(METERUSAGE_CSV_FILE)

    def GetMeterUsage(self, request: MeterUsageRequest, context) -> MeterUsageResponse:
        """Get meter usage data and return as MeterUsageResponse"""
        paginated_data = self.database.get_paginated_data(
            request.page_number, request.page_size
        )
        response_data = MeterUsageResponse(
            data=paginated_data["data"],
            page_number=request.page_number,
            page_size=request.page_size,
            total_pages=paginated_data["total_pages"],
        )
        return response_data
