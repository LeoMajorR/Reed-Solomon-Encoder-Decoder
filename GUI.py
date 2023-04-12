import sys

sys.path.append('..')

from reedSolo import RSCodec
import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Reed-Solomon Encoder/Decoder")
        self.master.geometry("700x600")
        self.master.configure(bg="#f0f0f0")
        self.master.resizable(False, False)
        self.pack(padx=20, pady=20)
        self.create_widgets()
        self.encoded_message = None
        self.decoded_message = None

    def create_widgets(self):
        self.heading = tk.Label(self,
                                text="Reed-Solomon Encoder/Decoder",
                                font=("Helvetica", 26),
                                pady=10)
        self.heading.pack()

        self.input_label = tk.Label(self,
                                    text="Input Message",
                                    font=("Helvetica", 16),
                                    pady=5)
        self.input_label.pack()

        self.input = tk.Entry(self, font=("Helvetica", 14))
        self.input.pack()

        self.encode = tk.Button(self,
                                text="Encode",
                                command=self.encode,
                                font=("Helvetica", 14),
                                bg="#4CAF50",
                                fg="white",
                                padx=10,
                                pady=5)
        self.encode.pack(pady=10)

        self.decode = tk.Button(self,
                                text="Decode",
                                command=self.decode,
                                font=("Helvetica", 14),
                                bg="#FFC107",
                                fg="white",
                                padx=10,
                                pady=5)
        self.decode.pack(pady=10)

        self.clear = tk.Button(self,
                               text="Clear",
                               command=self.clear,
                               font=("Helvetica", 14),
                               bg="#f44336",
                               fg="white",
                               padx=10,
                               pady=5)
        self.clear.pack(pady=10)

        self.exit = tk.Button(self,
                              text="Exit",
                              command=self.exit,
                              font=("Helvetica", 14),
                              bg="#2196F3",
                              fg="white",
                              padx=10,
                              pady=5)
        self.exit.pack(pady=10)

        self.message_label = tk.Label(self,
                                      text="Input Message",
                                      font=("Helvetica", 16),
                                      pady=5)
        self.message_label.pack()

        self.encoded_label = tk.Label(self,
                                      text="Encoded Message",
                                      font=("Helvetica", 16),
                                      pady=5)
        self.encoded_label.pack()

        self.decoded_label = tk.Label(self,
                                      text="Decoded Message",
                                      font=("Helvetica", 16),
                                      pady=5)
        self.decoded_label.pack()

    def encode(self):
        input = self.input.get()
        rs = RSCodec(10)
        self.encoded_message = rs.encode(input.encode())
        self.message_label.config(text="Input Message: " + input)
        self.encoded_label.config(text="Encoded Message: " +
                                  str(self.encoded_message))

    def decode(self):
        rs = RSCodec(10)
        self.decoded_message = rs.decode(self.encoded_message)
        self.decoded_label.config(text="Decoded Message: " +
                                  str(self.decoded_message[0].decode()))

    def clear(self):
        self.input.delete(0, 'end')
        self.message_label.config(text="Input Message")
        self.encoded_label.config(text="Encoded Message")
        self.decoded_label.config(text="Decoded Message")
        #delete the encoded and decoded messages
        self.encoded_message = None
        self.decoded_message = None

    def exit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()