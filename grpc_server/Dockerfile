FROM python:3-alpine

WORKDIR /app

RUN apk add --update --no-cache gcc linux-headers make musl-dev python3-dev g++
RUN pip install --upgrade poetry

ENV POETRY_VIRTUALENVS_CREATE=false
COPY grpc_server/poetry.lock grpc_server/pyproject.toml /app/
RUN poetry install

COPY grpc_server/src/ /app/src/
COPY grpc_server/meterusage.csv /app

COPY protobufs/ /app/protobufs/
RUN python -m grpc_tools.protoc -I /app/protobufs/ --python_out=/app/src/ \
    --pyi_out=/app/src/ --grpc_python_out=/app/src/ /app/protobufs/meterusage.proto

CMD ["python", "/app/src/main.py"]
