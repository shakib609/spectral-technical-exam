# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import meterusage_pb2 as meterusage__pb2


class MeterUsageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMeterUsage = channel.unary_unary(
                '/MeterUsage/GetMeterUsage',
                request_serializer=meterusage__pb2.MeterUsageRequest.SerializeToString,
                response_deserializer=meterusage__pb2.MeterUsageResponse.FromString,
                )


class MeterUsageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMeterUsage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeterUsageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMeterUsage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeterUsage,
                    request_deserializer=meterusage__pb2.MeterUsageRequest.FromString,
                    response_serializer=meterusage__pb2.MeterUsageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MeterUsage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeterUsage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMeterUsage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MeterUsage/GetMeterUsage',
            meterusage__pb2.MeterUsageRequest.SerializeToString,
            meterusage__pb2.MeterUsageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
