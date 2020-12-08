"""
COMP.CS 100
Tekijä:
Opiskelijanumero:
Sähköposti:
"""

from tkinter import *


def ROT13(text):
    regular_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_chars = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'

    txt = text
    rot13 = txt.maketrans(regular_chars, encrypted_chars)
    returni = txt.translate(rot13)

    return returni

def Caesar_Cipher(text):
    regular_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_chars = 'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA'

    txt = text
    caesar = txt.maketrans(regular_chars, encrypted_chars)
    returni = txt.translate(caesar)

    return returni

def Caesar_Cipher_decrypt(text):
    regular_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_chars = 'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA'
    txt = text
    caesar = txt.maketrans(encrypted_chars,regular_chars)
    returni = txt.translate(caesar)
    return returni

def hexdec(text):
    hexlist = []

    for i in range(0, len(text), 2):
        try:
            hexlist.append(f"0x{text[i]}{text[i + 1]} ")
        except:
            pass

    txt = ''.join(hexlist)
    try:
        enc = ''.join(chr(int(i, 16)) for i in txt.split())
        return (enc)
    except ValueError:
        return "Error: invalid input"

class Program:

    def __init__(self):

        self.__mainwindow = Tk()
        self.__mainwindow.title("Translator") #ikkunan otsikko
        self.__mainwindow.geometry("440x410")

        r = IntVar()
        r.set("1")

        """radiopainikkeet"""
        self.__value = r.get()

        self.__rot13 = Radiobutton(self.__mainwindow, text= "ROT-13", value="1", variable=r, command= lambda: [self.encryption(r.get()), self.decryption(r.get())]).grid(row = 2, column =1, sticky = 'W')

        self.__hex = Radiobutton(self.__mainwindow, text= "Hexadecimal", value="2", variable=r, command=lambda: [self.encryption(r.get()), self.decryption(r.get())]).grid(row = 3, column =1, sticky = 'W')

        self.__cesar = Radiobutton(self.__mainwindow, text= "Cesar cipher", value="3", variable=r, command=lambda:[self.encryption(r.get()),self.decryption(r.get())]).grid(row = 4, column =1, sticky = 'W')

        """tekstikentät"""
        self.__input = Text(self.__mainwindow, height=20, width=25,wrap= WORD)
        self.__input.insert(INSERT, "Input")
        self.__input.grid(row=1,column = 1)

        self.__output = Text(self.__mainwindow, height=20, width=25,wrap=WORD)
        self.__output.grid(row=1,column=2)

        """napit"""
        self.__encrypt_button = Button(self.__mainwindow, height=1,
                   width=14, text="Encrypt", command=lambda: self.__output.insert(INSERT, f"{self.encryption(r.get())}"), fg="green").grid(row=2, column =2, sticky ='W')

        self.__clear_button = Button(self.__mainwindow, height=1,
                   width=14, text="Clear", command=self.clear, fg= "#a69a00").grid(row=2, column =2, sticky ='E')

        self.__decrypt_button = Button(self.__mainwindow, height=1,
                   width=14, text="Decrypt", command=lambda: self.__output.insert(INSERT, f"{self.decryption(r.get())}"), fg="purple").grid(row=3, column =2, sticky ='W')

        self.__quit_button = Button(self.__mainwindow, text="Quit", height=1,
                   width=14, command=self.quit, fg= "red").grid(row=3, column =2, sticky ='E')

        """valikko"""
        menubar = Menu(self.__mainwindow)

        self.__mainwindow.config(menu=menubar)

        self.__filemenu = Menu(menubar)
        menubar.add_cascade(label="Menu", menu=self.__filemenu)

        self.__filemenu.add_command(label="Clear", command=self.clear)
        self.__filemenu.add_command(label="Help", command=self.help)
        self.__filemenu.add_command(label="About", command=self.about)
        self.__filemenu.add_separator()
        self.__filemenu.add_command(label="Quit", command=self.quit)

        self.__mainwindow.mainloop()

    def about(self):
        about = Tk()
        about.title("Help")
        about.geometry("400x300")
        label = Label(about, text="Translator\nVersion 1.\nPowered by Python 3.9.0").grid(sticky='N')

    def encryption(self, val):
        if val == 1: #ROT-13
            self.__output.delete('1.0', END)
            input = self.__input.get(1.0,END)
            encrypted = ROT13(input)
            return encrypted

        elif val == 2: #hexadecimal
            self.__output.delete('1.0', END)
            input = self.__input.get(1.0, END)
            s = input.encode().hex()
            return s

        elif val == 3: #Caesar cipher
            self.__output.delete('1.0', END)
            input = self.__input.get(1.0, END)
            encrypted = Caesar_Cipher(input)
            return encrypted

        else:
            self.__output.delete('1.0', END)
            input = self.__input.get(1.0, END)
            return input

    def decryption(self,val):
        if val == 1: #ROT-13
            self.__output.delete('1.0', END)
            input = self.__input.get(1.0, END)
            encrypted = ROT13(input)
            return encrypted

        elif val == 2: #Hexadecimal
            self.__output.delete('1.0', END)
            text = self.__input.get(1.0, END)
            input = self.__input.get(1.0, END)
            encrypted = hexdec(input)
            return encrypted

        elif val == 3: #Cesar
            self.__output.delete('1.0', END)
            input = self.__input.get(1.0, END)
            encrypted = Caesar_Cipher_decrypt(input)
            return encrypted

        else:
            self.__output.delete('1.0', END)
            input = self.__input.get(1.0, END)
            return input

    def clear(self):
        self.__input.delete('1.0', END)
        self.__output.delete('1.0', END)

    def donothing(self):
        pass

    def help(self):
        help = Tk()
        help.title("Help")
        help.geometry("450x410")

        headtxt = Label(help, text="HOW TO USE", font=("Times", 16)).pack(pady= 10)
        helptxt = "1. Choose the 'encryption' of your choice from left-bottom corner. \n" \
                  "2. Enter your message to the left textbox. \n" \
                  "3. Press encrypt to get the 'encrypted' message to the right textbox. \n" \
                  "\n" \
                  "ROT-13:\n" \
                  "A<->N, B<->O,C<->P,…,Z<->M\n" \
                  "Example:\nPlaintext: Hello world!\n" \
                  "Ciphertext: Uryyb jbeyq!\n" \
                  " \n" \
                  "Hexadecimal:\n" \
                  "Example:\nPlaintext: Hello world!\n" \
                  "Ciphertext: 48656c6c6f20776f726c64210a\n" \
                  "NOTE: while 'decrypting' input must be as above \n" \
                  " \n" \
                  "Cesar cipher: \n" \
                  "A<->B,B<->C,C<->D,…,Z<->A\n" \
                  "Example:\n" \
                  "Plaintext: Hello world!\n" \
                  "Ciphertext: Ifmmp xpsme!"

        label = Label(help, text=helptxt, justify="left", font=("Helvetica", 10)).pack()

    def quit(self):
        self.__mainwindow.destroy()

def main():
    Program()


if __name__ == "__main__":
    main()