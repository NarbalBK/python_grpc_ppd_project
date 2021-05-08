import tkinter as tk

class Tela:

    chatSend = None

    def __init__(self, master):
        master.title("putaria title")

        my_msg = tk.StringVar()  # For the messages to be sent.
        my_msg.set("")

        message_frame = tk.Frame(master)
        scrollbar = tk.Scrollbar(message_frame)
        self.message_list = tk.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.message_list.pack()
        message_frame.pack()

        entry_field = tk.Entry(master, textvariable=my_msg, background="gray", width=40)
        entry_field.bind("<Return>", self.send)
        entry_field.pack(side=tk.LEFT, fill=tk.BOTH)
        entry_field.pack()

        send_button = tk.Button(master, bg="blue", fg="white", text="Send", command=self.send)
        send_button.pack(side=tk.RIGHT, fill=tk.BOTH)
        send_button.pack()

        self.master = master

    def renderChatMessages(self, text):
        self.message_list.insert(tk.END, text)

    def send(self, event=None):
        print("send")
        self.chatSend()
        return None

    def setChatSend(self, func):
        self.chatSend = func

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

        send_button = tk.Button(master, bg="blue", fg="white", text="Send", command=self.send)
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
