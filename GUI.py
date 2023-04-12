import sys

sys.path.append('..')

from ReedSolomon import RSCodec
import tkinter as tk
import random, math


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Reed-Solomon Encoder/Decoder")
        self.master.geometry("1100x750")
        self.master.configure(bg="#f0f0f0")
        self.master.resizable(True, True)
        self.pack(padx=10, pady=10)
        self.create_widgets()
        self.encoded_message = None
        self.decoded_message = None
        self.error_correcting_bits = 10  #default value

    def create_widgets(self):
        self.heading = tk.Label(self,
                                text="Reed-Solomon Encoder/Decoder",
                                font=("Helvetica", 26),
                                pady=10)
        # align heading to center
        self.heading.pack(side="top", fill="x", expand=True)

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

        #italic font
        self.info_label = tk.Label(self,
                                   text=" ",
                                   font=("Helvetica", 14, "italic"),
                                   pady=5)
        self.info_label.pack()

        self.error_label = tk.Label(self,
                                    text="Add Error",
                                    font=("Helvetica", 16),
                                    pady=5)
        self.error_label.pack()
        self.error_input = tk.Entry(self, font=("Helvetica", 14))
        self.error_input.pack()

        self.add_error = tk.Button(self,
                                   text="Add Error",
                                   command=self.add_error,
                                   font=("Helvetica", 14),
                                   bg="#4CAF50",
                                   fg="white",
                                   padx=10,
                                   pady=5)
        self.add_error.pack(pady=10)

        self.decode = tk.Button(self,
                                text="Decode",
                                command=self.decode,
                                font=("Helvetica", 14),
                                bg="#FFC107",
                                fg="white",
                                padx=10,
                                pady=5)
        self.decode.pack(pady=10)

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

        self.error_message_label = tk.Label(self,
                                            text="Error Message",
                                            font=("Helvetica", 16),
                                            pady=5)

        self.error_message_label.pack()

        self.decoded_label = tk.Label(self,
                                      text="Decoded Message",
                                      font=("Helvetica", 16),
                                      pady=5)
        self.decoded_label.pack()

        self.clear = tk.Button(self,
                               text="Clear",
                               command=self.clear,
                               font=("Helvetica", 14),
                               bg="#f44336",
                               fg="white",
                               padx=10,
                               pady=5)
        self.clear.pack(side=tk.LEFT, pady=10)

        self.exit = tk.Button(self,
                              text="Exit",
                              command=self.exit,
                              font=("Helvetica", 14),
                              bg="#2196F3",
                              fg="white",
                              padx=10,
                              pady=5)
        #place button at same level as clear button
        self.exit.pack(side=tk.RIGHT, pady=10)

    def encode(self):
        input = self.input.get()
        rs = RSCodec(self.error_correcting_bits)
        self.encoded_message = rs.encode(input.encode())
        n = len(self.encoded_message)
        k = len(input.encode())
        t = math.floor((n - k) / 2)
        self.message_label.config(text="Input Message: " + input)
        self.encoded_label.config(text="Encoded Message: " +
                                  str(self.encoded_message)[11:-1])
        self.info_label.config(text="Given message of length k = " + str(k) +
                               " codeword length n = " + str(n) +
                               " it can correct up to t = floor(n-k)/2 = " +
                               str(t) + " errors",
                               borderwidth=2,
                               relief="solid",
                               bg="#e0e0e0")

    def add_error(self):
        n = self.error_input.get()
        try:
            n = int(n)
        except ValueError:
            self.error_input.delete(0, tk.END)
            self.error_input.insert(0, "Enter a positive integer")
            return
        arr = random.sample(range(0, len(self.encoded_message)), n)
        for i in range(n):
            pos = arr[i]
            self.encoded_message[pos] = random.randint(0, 255)
            self.error_message_label.config(text="Error Message: " +
                                            str(self.encoded_message)[11:-1])

    def decode(self):
        rs = RSCodec(10)
        try:
            self.decoded_message = rs.decode(self.encoded_message)
            self.decoded_label.config(text="Decoded Message: " +
                                      str(self.decoded_message[0].decode()),
                                      fg="green")
        except:
            self.decoded_label.config(text="Decoded Message: " +
                                      "Too many errors to correct!!!!",
                                      fg="red")

    def clear(self):
        self.input.delete(0, 'end')
        self.message_label.config(text="Input Message")
        self.encoded_label.config(text="Encoded Message")
        self.decoded_label.config(text="Decoded Message")
        self.error_message_label.config(text="Error Message")
        self.info_label.config(text=" ")
        self.error_input.delete(0, 'end')
        self.error_correction_bits.delete(0, 'end')
        #delete the encoded and decoded messages
        self.encoded_message = None
        self.decoded_message = None

    def exit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()