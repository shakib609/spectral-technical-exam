# Spectral Technical Exam

This repository contains the technical exam solution given by Spectral. It has three main components.
- gRPC Server
- FastApi Server - gRPC Client
- HTML Page


## gRPC Server

The gRPC server resides on the `grpc_server` directory. The server reads data from the `meterusage.csv` file, and serves it in a paginated way for its clients.


## FastAPI Server - gRPC Client

The FastAPI Server resides on the `grpc_client_http` directory. The server exposes an API for the clients to get the time-series data from the gRPC server.

## HTML Page

The HTML page which communicates with the FastAPI server resides on the `ui` directory. The `index.html` file can be opened directly after starting the servers. The page is designed to fetch the data asynchronously. It fetches 100 items per page.

### Pre-requisites

- docker
- docker-compose
- python 3.11 (For integration tests)
- poetry (For integration tests)

### Running the Server

To run the server locally simply build the server images and run them using docker compose. You can run the below commands.

```
docker compose build
docker compose up
```

The above command will start up the servers on below host and port respectively:
- grpc_server: localhost:50051
- grpc_client_http: localhost:8080

You can check the fastapi API documentations here: http://localhost:8080/docs


### Running Unit Tests

To run the unit-tests for the servers, first build the images using `docker compose build`

Then the unit-tests can be run for the servers with the below commands respectively.
- grpc_server - `docker compose run grpc_server pytest`
- grpc_client_http - `docker compose run grpc_client_http pytest` 


### Running Integration Tests

To run the integration-tests for the servers run the below commands

- build the docker images - `docker compose build`
- change into the `integration_tests` directory - `cd integration_tests`
- Install dependencies - `poetry install`
- Run tests - `poetry run pytest`
