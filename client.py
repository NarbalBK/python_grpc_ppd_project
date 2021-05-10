from __future__ import print_function
import logging

import grpc
import threading
import tkinter as tk

from chatui import *

import chat_pb2
import chat_pb2_grpc

class ChatClient:

    ui = None
    stub = None
    username = None
    corDoJogador = None

    def __init__(self):
        logging.basicConfig()
        login = Login(tk.Tk())
        self.username = login.username
        run_grpc_thread = threading.Thread(target=self.run_grpc, daemon=True)
        run_grpc_thread.start()

    def run_grpc(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = chat_pb2_grpc.ChatStub(channel)

        receive_messages_thread = threading.Thread(target=self.receive_messages, daemon=True)
        receive_messages_thread.start()

        refresh_tabuleiro_thread = threading.Thread(target=self.RefreshTabuleiro, daemon=True)
        refresh_tabuleiro_thread.start()
            
    def send_messages(self, text=""):
        print("[SEND MESSAGE]")
        self.stub.SendMessage(chat_pb2.ChatMessage(name=self.username, message=text))

    def cores_disponiveis(self):
        print("[CORES DISPONIVEIS]")
        response = self.stub.CoresDisponiveis(chat_pb2.Empty())
        return response.data

    def choice_color(self, color):
        print("[CHOICE COLOR]")
        response = self.stub.ChoiceColor(chat_pb2.Cor(cor=color))
        if response.status:
            self.corDoJogador = color
        return response.status

    def TurnoAtual(self):
        print("[TURNO ATUAL]")
        response = self.stub.TurnoAtual(chat_pb2.Empty())
        return response.cor

    def TrocarDeTurno(self, color):
        print("[TROCA DE TURNO]")
        response = self.stub.TrocarDeTurno(chat_pb2.Cor(cor=color))
        return response.status

    def TabuleiroAtual(self):
        print("[TABULEIRO ATUAL]")
        response = self.stub.TabuleiroAtual(chat_pb2.Empty())
        tabuleiro = [
            response.line1,
            response.line2, 
            response.line3, 
            response.line4, 
            response.line5, 
            response.line6, 
            response.line7, 
            response.line8]
        return tabuleiro

    def ChangeTabuleiro(self, color, pos):
        print("[CHANGE TABULEIRO]")
        response = self.stub.ChangeTabuleiro(chat_pb2.Pos(cor=color, pos=pos))
        return response.status

    def receive_messages(self):
        if not self.stub:
            return None

        print("[RECEIVE MESSAGE]")
        for message in self.stub.ReceiveMessage(chat_pb2.Empty()):
            print("Chat client received: " +message.name +" "+ message.message)
            if self.ui != None:
                self.ui.renderChatMessages(message.name +" "+ message.message)

    def RefreshTabuleiro(self):
        if not self.stub:
            return None

        print("[REFRESH TABULEIRO]")
        for message in self.stub.RefreshTabuleiro(chat_pb2.Empty()):
            if self.ui != None:
                self.ui.renderTabuleiro()

    def ui_reference(self, exUi):
        self.ui = exUi
        self.ui.start_root()

if __name__ == '__main__':
    print("[MAIN]")
    chatClient = ChatClient()
    ui = Tela(tk.Tk(), chatClient)
    chatClient.ui_reference(ui)
    
    
    