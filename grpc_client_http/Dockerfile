FROM python:3-alpine

WORKDIR /app

RUN apk add --update --no-cache gcc linux-headers make musl-dev python3-dev g++
RUN pip install --upgrade poetry

ENV POETRY_VIRTUALENVS_CREATE=false
COPY grpc_client_http/poetry.lock grpc_client_http/pyproject.toml /app/
RUN poetry install

COPY grpc_client_http/src/ /app/
COPY protobufs/ /app/protobufs/

RUN python -m grpc_tools.protoc -I /app/protobufs/ --python_out=/app/ \
    --pyi_out=/app/ --grpc_python_out=/app/ /app/protobufs/meterusage.proto

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
