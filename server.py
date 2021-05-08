from concurrent import futures
import logging
import time

import grpc

import chat_pb2
import chat_pb2_grpc

class Chat(chat_pb2_grpc.ChatServicer):
    def __init__(self):
        self._history = []
        self.last_index = 1

    def SendMessage(self, request, context):
        print("[SEND MESSAGE]")
        self._history.append(request)
        self.last_index = 0
        return chat_pb2.Empty()

    def ReceiveMessage(self, request_iterator, context):
        print("[RECEIVE MESSAGE]")
        while True:
            # Send all messages from the queue of unsent
            while self.last_index < 1:
                message = self._history[0]
                # yield - it's like endless return.
                # The feature will return values over and over again when called yield.
                time.sleep(0.02)
                self._history = []
                self.last_index = 1
                yield message
            # Add a little sleep to reduce the load on the server by constantly checking new messages
            time.sleep(0.02)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(Chat(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
