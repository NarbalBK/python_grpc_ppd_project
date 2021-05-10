from concurrent import futures
import logging
import time
from google.protobuf import message

import grpc

import chat_pb2
import chat_pb2_grpc

class Chat(chat_pb2_grpc.ChatServicer):

    def __init__(self):
        self._history = []
        self.last_index = 1

        self.refresh = []
        self.refresh_index = 1

        self.turno = 0 # 0 = preto
        self.coresDisponiveis = [0 , 1] # 0 = preto e 1 = branco
        self.tabuleiro = self.make_tabuleiro()

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
                time.sleep(0.03)
                self._history = []
                self.last_index = 1
                yield message
            # Add a little sleep to reduce the load on the server by constantly checking new messages
            time.sleep(0.05)

    def RefreshTabuleiro(self, request_iterator, context):
        print("[REFRESH TABULEIRO]")
        while True:
            # Send all messages from the queue of unsent
            while self.refresh_index < 1:
                message = self.refresh[0]
                # yield - it's like endless return.
                # The feature will return values over and over again when called yield.
                time.sleep(0.03)
                self.refresh = []
                self.refresh_index = 1
                yield message
            # Add a little sleep to reduce the load on the server by constantly checking new messages
            time.sleep(0.05)

    def CoresDisponiveis(self, request, context):
        print("[CORES DISPONOVEIS]")
        response = chat_pb2.Cores(data=self.coresDisponiveis)
        return response

    def ChoiceColor(self, request, context):
        print("[CHOICE COLOR]")
        if request.cor in self.coresDisponiveis:
            self.coresDisponiveis.remove(request.cor)
            return chat_pb2.Status(status=True)
        return chat_pb2.Status(status=False)

    def TurnoAtual(self, request, context):
        print("[TURNO ATUAL]")
        return chat_pb2.Cor(cor=self.turno)

    def TrocarDeTurno(self, request, context):
        print("[TROCAR DE TURNO]")
        if request.cor == self.turno:
            if request.cor == 0:
                self.turno = 1
            if request.cor == 1:
                self.turno = 0
            return chat_pb2.Status(status=True)
        return chat_pb2.Status(status=False)

    def TabuleiroAtual(self, request, context):
        print("[TABULEIRO ATUAL]")
        return chat_pb2.Tabuleiro(
            line1=self.tabuleiro[0],
            line2=self.tabuleiro[1],
            line3=self.tabuleiro[2],
            line4=self.tabuleiro[3],
            line5=self.tabuleiro[4],
            line6=self.tabuleiro[5],
            line7=self.tabuleiro[6],
            line8=self.tabuleiro[7])

    def ChangeTabuleiro(self, request, context):
        print("[CHANGE TABULEIRO]")
        pos = request.pos
        color = request.cor
        self.tabuleiro[pos[0]][pos[1]] = color

        self.refresh.append(chat_pb2.Empty())
        self.refresh_index = 0
        return chat_pb2.Status(status=True)

    def make_tabuleiro(self):
        mtx_tabuleiro = []
        tb_line = []
        for i in range(8):
            for j in range(8):
                tb_line.append(-1)
            mtx_tabuleiro.append(tb_line)
            tb_line = []
        mtx_tabuleiro[3][3] = 1
        mtx_tabuleiro[4][3] = 0
        mtx_tabuleiro[3][4] = 0
        mtx_tabuleiro[4][4] = 1
        return mtx_tabuleiro

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(Chat(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
