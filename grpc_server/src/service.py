import csv

from meterusage_pb2 import MeterUsageData, MeterUsageResponse
from meterusage_pb2_grpc import MeterUsageServicer
from utils import convert_string_to_timestamp

METERUSAGE_CSV_FILE = "meterusage.csv"


def get_meter_usage_data_from_csv_file(path=METERUSAGE_CSV_FILE):
    """Reads meter usage data from `path` csv file and returns the data"""
    with open(path) as csv_file:
        response_data = MeterUsageResponse()
        reader = csv.DictReader(csv_file)
        for row in reader:
            meter_data = MeterUsageData(
                time=convert_string_to_timestamp(row["time"]),
                meterusage=float(row["meterusage"]),
            )
            response_data.data.append(meter_data)
        return response_data


class MeterUsageService(MeterUsageServicer):
    def GetMeterUsage(self, request, context) -> MeterUsageResponse:
        """Get meter usage data and return as MeterUsageResponse"""
        response_data = get_meter_usage_data_from_csv_file(METERUSAGE_CSV_FILE)
        return response_data
