from google.protobuf.timestamp_pb2 import Timestamp

from datetime import datetime


def convert_string_to_timestamp(timestamp_str: str) -> Timestamp:
    time = Timestamp()
    formatted_time_str = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    time.FromDatetime(formatted_time_str)
    return time
