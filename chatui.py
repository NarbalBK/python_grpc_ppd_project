import tkinter as tk
from tkmacosx import Button
from functools import partial

class Tela:

    corDoJogador = None
    qtdBrancas = 0
    qtdPretas = 0

    def __init__(self, master, chatController):
        master.title("putaria title")
        master.geometry("1080x600")

        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("")

        chat_frame = tk.Frame(master, width=200, height=800) #* * * *

        message_frame = tk.Frame(chat_frame) # * * *

        scrollbar = tk.Scrollbar(message_frame)
        self.message_list = tk.Listbox(message_frame, width=52, height=25, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.message_list.pack()

        message_frame.pack() # * * *

        input_frame = tk.Frame(chat_frame) # * * *

        entry_field = tk.Entry(input_frame, textvariable=self.my_msg, background='gray', width=40)
        entry_field.bind("<Return>", self.send)
        entry_field.pack(side=tk.LEFT)
        entry_field.pack()
        send_button = Button(input_frame, bg="blue", fg="white", text="Enviar", command=self.send)
        send_button.pack(side=tk.RIGHT)
        send_button.pack()

        input_frame.pack() # * * *

        input_menu = tk.Frame(chat_frame, width=20, height=20) # * * *

        lbl_cor = tk.Label(input_menu, text="Com qual cor você deseja jogar?")
        lbl_cor.pack()

        frame_button = tk.Frame(input_menu) # * *
        self.bt_preto = Button(frame_button, bg="white", fg="black", text="Preto", command=lambda: self.sendColorChoice(0))
        self.bt_branco = Button(frame_button, bg="white", fg="black", text="Branco", command=lambda: self.sendColorChoice(1))
        self.bt_preto.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.bt_branco.pack(side=tk.LEFT, fill=tk.BOTH)
        self.bt_preto.pack()
        self.bt_branco.pack()
        frame_button.pack() # * *

        lbl_troca = tk.Label(input_menu, text="Você deseja passar o turno?")
        lbl_troca.pack()
        bt_troca = Button(input_menu, bg="white", fg="black", text="Passar turno!", command=self.TrocarDeTurno)
        bt_troca.pack()

        input_menu.pack() # * * *

        chat_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        chat_frame.pack()  # * * * *

        self.imgBlank = tk.PhotoImage(file="./img/semBolinha.gif")
        self.imgBlack = tk.PhotoImage(file="./img/preto.gif")
        self.imgWhite = tk.PhotoImage(file="./img/branco.gif")

        tabuleiro = tk.Frame(master, width=1000, height=800) # * * * *
        self.mtx_tb_buttons = []
        tb_buttons_line = []
        for i in range(8):
            for j in range(8):
                tb_buttons_line.append(Button(tabuleiro, bg="gray", fg="gray", image=self.imgBlank, command=partial(self.tabuleiroActions, [j, i])))
                tb_buttons_line[j].place(x=i*80, y=j*70)
            self.mtx_tb_buttons.append(tb_buttons_line)
            tb_buttons_line = []
        tabuleiro.pack(side=tk.RIGHT, fill=tk.BOTH)

        tabuleiro.pack() # * * * *
            
        self.master = master
        self.chatController = chatController

        self.buttonActivation()
        self.renderTabuleiro()

    def tabuleiroActions(self, pos):
        print("[TABULEIRO ACTIONS]")
        print(pos)

    def TabuleiroAtual(self):
        print("[UI TABULEIRO ATUAL]")
        return self.chatController.TabuleiroAtual()

    def renderChatMessages(self, text):
        self.message_list.insert(tk.END, text)

    def renderTabuleiro(self):
        print("[UI RENDER TABULEIRO]")
        self.qtdBrancas = 0
        self.qtdPretas = 0
        tabuleiro = self.TabuleiroAtual()
        for i in range(8):
            for j in range(8):
                if tabuleiro[i][j] == -1:
                    self.mtx_tb_buttons[i][j]["image"] = self.imgBlank
                elif tabuleiro[i][j] == 0:
                    self.mtx_tb_buttons[i][j]["image"] = self.imgBlack
                    self.qtdPretas += 1
                elif tabuleiro[i][j] == 1:
                    self.mtx_tb_buttons[i][j]["image"] = self.imgWhite
                    self.qtdBrancas += 1

    def send(self, event=None):
        print("send")
        self.chatController.send_messages(self.my_msg.get())
        self.my_msg.set("")
        return None

    def start_root(self):
        self.master.mainloop()

    def sendColorChoice(self, color):
        print("[SEND COLOR CHOICE]")
        response = self.chatController.choice_color(color)
        print(response)
        if response:
            self.buttonActivation()
            if color == 0:
                self.bt_branco["state"] = "disabled"
            if color == 1:
                self.bt_preto["state"] = "disabled"
            self.corDoJogador = color

    def buttonActivation(self):
        print("[BUTTON ACTIVATION]")
        coresDisponiveis = self.chatController.cores_disponiveis()
        print(coresDisponiveis)
        if 0 in coresDisponiveis:
            if self.bt_preto["state"] != "normal":
                self.bt_preto["state"] = "normal"
        else:
            if self.bt_preto["state"] != "disabled":
                self.bt_preto["state"] = "disabled"

        if 1 in coresDisponiveis:
            if self.bt_branco["state"] != "normal":
                self.bt_branco["state"] = "normal"
        else:
            if self.bt_branco["state"] != "disabled":
                self.bt_branco["state"] = "disabled"

    def TurnoAtual(self):
        print("[UI TURNO ATUAL]")
        response = self.chatController.TurnoAtual()
        return response

    def TrocarDeTurno(self):
        print("[UI TROCAR DE TURNO]")
        if self.corDoJogador == None:
            return self.empty()
        response = self.chatController.TrocarDeTurno(self.corDoJogador)
        if response:
            print(self.TurnoAtual())

    def empty(self, event=None):
        pass

class Login:

    username = "anonimo: "

    def __init__(self, master):
        master.title("putaria login")
        master.geometry("200x200")

        self.my_msg = tk.StringVar()
        self.my_msg.set("")

        login_frame = tk.Frame(master, height=100, width=100)
        login_frame.pack()
        lbl = tk.Label(login_frame, text="Insira o seu apelido")
        lbl.pack()
        entry_field = tk.Entry(master, textvariable=self.my_msg, background="gray", width=40)
        entry_field.bind("<Return>", self.send)
        # entry_field.pack(side=tk.CENTER)
        entry_field.pack()

        send_button = Button(master, bg="blue", fg="white", text="Ok", command=self.send)
        send_button.pack(side=tk.RIGHT, fill=tk.BOTH)
        send_button.pack()

        self.master = master
        self.master.mainloop()

    def send(self, event=None):
        print("SAIR")
        if self.my_msg.get() != "":
            self.username = self.my_msg.get()+": "
        self.end_root()
        return None

    def end_root(self):
        self.master.destroy()
