# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_pb2 as chat__pb2


class ChatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/chat.Chat/SendMessage',
                request_serializer=chat__pb2.ChatMessage.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )
        self.ReceiveMessage = channel.unary_stream(
                '/chat.Chat/ReceiveMessage',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.ChatMessage.FromString,
                )
        self.CoresDisponiveis = channel.unary_unary(
                '/chat.Chat/CoresDisponiveis',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Cores.FromString,
                )
        self.ChoiceColor = channel.unary_unary(
                '/chat.Chat/ChoiceColor',
                request_serializer=chat__pb2.Cor.SerializeToString,
                response_deserializer=chat__pb2.Status.FromString,
                )
        self.TurnoAtual = channel.unary_unary(
                '/chat.Chat/TurnoAtual',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Cor.FromString,
                )
        self.TrocarDeTurno = channel.unary_unary(
                '/chat.Chat/TrocarDeTurno',
                request_serializer=chat__pb2.Cor.SerializeToString,
                response_deserializer=chat__pb2.Status.FromString,
                )
        self.TabuleiroAtual = channel.unary_unary(
                '/chat.Chat/TabuleiroAtual',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Tabuleiro.FromString,
                )
        self.ChangeTabuleiro = channel.unary_unary(
                '/chat.Chat/ChangeTabuleiro',
                request_serializer=chat__pb2.Pos.SerializeToString,
                response_deserializer=chat__pb2.Status.FromString,
                )
        self.RefreshTabuleiro = channel.unary_stream(
                '/chat.Chat/RefreshTabuleiro',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Empty.FromString,
                )


class ChatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CoresDisponiveis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChoiceColor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TurnoAtual(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrocarDeTurno(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TabuleiroAtual(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeTabuleiro(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshTabuleiro(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=chat__pb2.ChatMessage.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
            'ReceiveMessage': grpc.unary_stream_rpc_method_handler(
                    servicer.ReceiveMessage,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.ChatMessage.SerializeToString,
            ),
            'CoresDisponiveis': grpc.unary_unary_rpc_method_handler(
                    servicer.CoresDisponiveis,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Cores.SerializeToString,
            ),
            'ChoiceColor': grpc.unary_unary_rpc_method_handler(
                    servicer.ChoiceColor,
                    request_deserializer=chat__pb2.Cor.FromString,
                    response_serializer=chat__pb2.Status.SerializeToString,
            ),
            'TurnoAtual': grpc.unary_unary_rpc_method_handler(
                    servicer.TurnoAtual,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Cor.SerializeToString,
            ),
            'TrocarDeTurno': grpc.unary_unary_rpc_method_handler(
                    servicer.TrocarDeTurno,
                    request_deserializer=chat__pb2.Cor.FromString,
                    response_serializer=chat__pb2.Status.SerializeToString,
            ),
            'TabuleiroAtual': grpc.unary_unary_rpc_method_handler(
                    servicer.TabuleiroAtual,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Tabuleiro.SerializeToString,
            ),
            'ChangeTabuleiro': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeTabuleiro,
                    request_deserializer=chat__pb2.Pos.FromString,
                    response_serializer=chat__pb2.Status.SerializeToString,
            ),
            'RefreshTabuleiro': grpc.unary_stream_rpc_method_handler(
                    servicer.RefreshTabuleiro,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat.Chat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.Chat/SendMessage',
            chat__pb2.ChatMessage.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/chat.Chat/ReceiveMessage',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.ChatMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CoresDisponiveis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.Chat/CoresDisponiveis',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Cores.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChoiceColor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.Chat/ChoiceColor',
            chat__pb2.Cor.SerializeToString,
            chat__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TurnoAtual(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.Chat/TurnoAtual',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Cor.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrocarDeTurno(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.Chat/TrocarDeTurno',
            chat__pb2.Cor.SerializeToString,
            chat__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TabuleiroAtual(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.Chat/TabuleiroAtual',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Tabuleiro.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeTabuleiro(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.Chat/ChangeTabuleiro',
            chat__pb2.Pos.SerializeToString,
            chat__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RefreshTabuleiro(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/chat.Chat/RefreshTabuleiro',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
