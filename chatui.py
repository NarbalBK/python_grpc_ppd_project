import tkinter as tk
from tkmacosx import Button

class Tela:

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
        bt_preto = Button(frame_button, bg="white", fg="black", text="Preto", command=self.empty)
        bt_branco = Button(frame_button, bg="white", fg="black", text="Branco", command=self.empty)
        bt_preto.pack(side=tk.RIGHT, fill=tk.BOTH)
        bt_branco.pack(side=tk.LEFT, fill=tk.BOTH)
        bt_preto.pack()
        bt_branco.pack()
        frame_button.pack() # * *

        lbl_troca = tk.Label(input_menu, text="Você deseja passar o turno?")
        lbl_troca.pack()
        bt_troca = Button(input_menu, bg="white", fg="black", text="Passar turno!", command=self.empty)
        bt_troca.pack()

        input_menu.pack() # * * *

        chat_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        chat_frame.pack()  # * * * *

        imgBlank = tk.PhotoImage(file="./img/semBolinha.gif")

        tabuleiro = tk.Frame(master, width=1000, height=800) # * * * *
        for i in range(8):
            for j in range(8):
                bt = Button(tabuleiro, bg="gray", fg="gray", image=imgBlank).place(x=i*80, y=j*70)
        tabuleiro.pack(side=tk.RIGHT, fill=tk.BOTH)

        tabuleiro.pack() # * * * *

        self.master = master
        self.chatController = chatController

    def renderChatMessages(self, text):
        self.message_list.insert(tk.END, text)

    def send(self, event=None):
        print("send")
        self.chatController.send_messages(self.my_msg.get())
        self.my_msg.set("")
        return None

    def start_root(self):
        self.master.mainloop()

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
