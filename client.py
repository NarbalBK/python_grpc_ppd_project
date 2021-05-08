from __future__ import print_function
import logging
from google.protobuf import message

import grpc
import threading

import chat_pb2
import chat_pb2_grpc

stub = None

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        global stub
        stub = chat_pb2_grpc.ChatStub(channel)
        listen_messages_thread = threading.Thread(target=start_listen_messages, daemon=True)
        listen_messages_thread.start()
        while True:
            print("[SEND MESSAGE]")
            stub.SendMessage(chat_pb2.ChatMessage(name='client', message="fuck you"))
            input()

def start_listen_messages():
    global stub
    if not stub:
        return
    print("[RECEIVE MESSAGE]")
    for message in stub.ReceiveMessage(chat_pb2.Empty()):
        print("Chat client received: " +message.name +" - "+ message.message)
 
if __name__ == '__main__':
    logging.basicConfig()
    run()