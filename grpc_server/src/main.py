from concurrent import futures
import logging
import os

import grpc

from meterusage_pb2_grpc import add_MeterUsageServicer_to_server
from service import MeterUsageService

PORT = int(os.environ.get("PORT"))


def serve():
    print(f"Starting server on port: {PORT}")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MeterUsageServicer_to_server(MeterUsageService(), server)
    server.add_insecure_port(f"0.0.0.0:{PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
