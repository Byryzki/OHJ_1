"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 050282836
Name:       Pyry Laine
Email:      pyry.j.laine@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        self.__ikkuna = Tk()

        self.__nro = 0

        self.__current_value = Label(self.__ikkuna, text= self.__nro)   # Label displaying the current value of the counter.
        self.__current_value.grid(row=0, column= 2)

        self.__reset_button = Button(self.__ikkuna, text= "Reset", command= self.reset)  # Button which resets counter to zero.
        self.__reset_button.grid(row= 1, column= 0)

        self.__increase_button = Button(self.__ikkuna, text= "Increase", command= self.increase)  # Button which increases the value of the counter by one.
        self.__increase_button.grid(row= 1, column= 1)

        self.__decrease_button = Button(self.__ikkuna, text= "Decrease", command= self.decrease)  # Button which decreases the value of the counter by one.
        self.__decrease_button.grid(row= 1, column= 3)

        self.__quit_button = Button(self.__ikkuna, text= "Quit", command= self.quit)      # Button which quits the program.
        self.__quit_button.grid(row=1, column= 4)

        self.__ikkuna.mainloop()

        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

    # TODO: Implement the rest of the needed methods here.
    def quit(self):
        self.__ikkuna.destroy()

    def increase(self):
        self.__nro += 1
        self.__current_value.config(text= self.__nro)

    def decrease(self):
        self.__nro -= 1
        self.__current_value.config(text= self.__nro)

    def reset(self):
        self.__nro = 0
        self.__current_value.config(text= self.__nro)

def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
