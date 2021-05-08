import tkinter as tk

class Tela:
    def __init__(self):
        root = tk.Tk()
        root.title("putaria title")

        my_msg = tk.StringVar()  # For the messages to be sent.
        my_msg.set("Type your messages here.")

        message_frame = tk.Frame(root)
        scrollbar = tk.Scrollbar(message_frame)
        self.message_list = tk.Listbox(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.message_list.pack()
        message_frame.pack()

        entry_field = tk.Entry(root, textvariable=my_msg)
        entry_field.bind("<Return>", self.send)
        entry_field.pack()
        send_button = tk.Button(root, text="Send", command=self.send)
        send_button.pack()

        root.mainloop()

    def renderChatMessages(self, text):
        self.message_list.insert(tk.END, text)

    def send(self):
        print("send")
        self.message_list.insert(tk.END, "text")
        return None