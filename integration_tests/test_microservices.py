import csv
from datetime import datetime
import subprocess
import time

import httpx

GRPC_CLIENT_HOST = "localhost"
GRPC_CLIENT_HOST_PORT = "8080"
CSV_FILE_PATH = "../meterusage.csv"


def setup_module(module):
    # Start the services
    subprocess.check_call(["docker", "compose", "up", "-d"])
    time.sleep(10)


def teardown_module(module):
    # Stop the services
    subprocess.check_call(["docker", "compose", "down"])


def read_data_from_csv(file_path):
    data = []
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            time = row["time"]
            meterusage = row["meterusage"]
            parsed_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            meterusage_data = {
                "time": parsed_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "meterusage": float(meterusage),
            }
            data.append(meterusage_data)
        return data


def get_response_from_grpc_client(page_number: int, page_size: int):
    response = httpx.get(
        f"http://{GRPC_CLIENT_HOST}:{GRPC_CLIENT_HOST_PORT}/api/v1/meterusage/?page_number={page_number}&page_size={page_size}"
    )
    return response



def test_csv_data_is_being_returned_from_file():
    page_number = 1
    page_size = 100
    response = get_response_from_grpc_client(page_number=page_number, page_size=page_size)
    parsed_response = response.json()
    response_data = parsed_response["data"]

    csv_data = read_data_from_csv(CSV_FILE_PATH)

    assert response.status_code == 200
    assert csv_data[0] == response_data[0]
    assert csv_data[1] == response_data[1]
    assert csv_data[99] == response_data[99]


def test_pagination_is_returning_appropriate_csv_data():
    # Read the data from the CSV file
    csv_data = read_data_from_csv(CSV_FILE_PATH)

    # Send a request to the FastAPI service
    page_size = 100
    response_1 = get_response_from_grpc_client(page_number=1, page_size=page_size)
    parsed_response_1 = response_1.json()
    response_1_data = parsed_response_1["data"]

    response_2 = get_response_from_grpc_client(page_number=2, page_size=page_size)
    parsed_response_2 = response_2.json()
    response_2_data = parsed_response_2["data"]


    # Check the response
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert csv_data[0] == response_1_data[0]
    assert csv_data[99] == response_1_data[99]
    assert csv_data[100] == response_2_data[0]
    assert csv_data[199] == response_2_data[99]
