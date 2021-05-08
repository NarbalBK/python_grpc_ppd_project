from __future__ import print_function
import logging

import grpc
import threading
import time

from chatui import Tela

import chat_pb2
import chat_pb2_grpc

class ChatClient:

    ui = Tela()
    stub = None

    def __init__(self):
        logging.basicConfig()
        
        run_grpc_thread = threading.Thread(target=self.run_grpc, daemon=True)
        run_grpc_thread.start()

        
    def run_grpc(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            self.stub = chat_pb2_grpc.ChatStub(channel)

            receive_messages_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_messages_thread.start()

            self.send_messages()
            
    def send_messages(self):
        while True:
            print("[SEND MESSAGE]")
            self.stub.SendMessage(chat_pb2.ChatMessage(name='client', message="fuck you"))
            print(self.ui)
            # if ui != None:
            #     ui.renderChatMessages("fuck you")
            time.sleep(2)

    def receive_messages(self):
        if not self.stub:
            return None

        print("[RECEIVE MESSAGE]")
        for message in self.stub.ReceiveMessage(chat_pb2.Empty()):
            # ui.renderChatMessages(message.name +" - "+ message.message)
            print("Chat client received: " +message.name +" - "+ message.message)

if __name__ == '__main__':
    print("JA CHEGOU O DISCO VOADOR")
    chatClient = ChatClient()
    
    
    