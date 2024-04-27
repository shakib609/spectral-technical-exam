import csv
from typing import Any

from meterusage_pb2 import MeterUsageData
from utils import convert_string_to_timestamp


class Database:
    """
    Database class to load data from CSV file and store it in memory
    """

    data: list[MeterUsageData] = []

    def load_data_from_csv_file(self, path: str) -> None:
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                meter_data = MeterUsageData(
                    time=convert_string_to_timestamp(row["time"]),
                    meterusage=float(row["meterusage"]),
                )
                self.data.append(meter_data)

    def get_paginated_data(
        self,
        page_number: int,
        page_size: int,
    ) -> dict[str, Any]:
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        total_pages = (len(self.data) // page_size) + 1
        return {
            "data": self.data[start_index:end_index],
            "total_pages": total_pages,
        }
