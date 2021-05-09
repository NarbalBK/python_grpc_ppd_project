import tkinter as tk
from tkmacosx import Button

class Tela:

    def __init__(self, master, chatController):
        master.title("putaria title")

        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("")

        message_frame = tk.Frame(master)
        scrollbar = tk.Scrollbar(message_frame)
        self.message_list = tk.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.message_list.pack()
        message_frame.pack()

        input_frame = tk.Frame(master)
        entry_field = tk.Entry(input_frame, textvariable=self.my_msg, background='gray', width=40)
        entry_field.bind("<Return>", self.send)
        entry_field.pack(side=tk.LEFT, fill=tk.BOTH)
        entry_field.pack()
        send_button = Button(master, bg="blue", fg="white", text="Enviar", command=self.send)
        send_button.pack(side=tk.RIGHT, fill=tk.BOTH)
        send_button.pack()
        input_frame.pack()

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

class Login:

    username = "anonimo: "

    def __init__(self, master):
        master.title("putaria login")

        self.my_msg = tk.StringVar()
        self.my_msg.set("")

        login_frame = tk.Frame(master, height=50, width=50)
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
