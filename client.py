from __future__ import print_function
import logging

import grpc

import chat_pb2
import chat_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.SendMessage(chat_pb2.ChatMessage(name='client', message="fuck you"))
    print("Chat client received: " + response.name +" - "+ response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()