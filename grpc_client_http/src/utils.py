from datetime import datetime, timezone


def convert_timestamp_to_iso(timestamp_in_seconds: int) -> str:
    timestamp = datetime.fromtimestamp(timestamp_in_seconds, timezone.utc)
    iso_timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
    return iso_timestamp
