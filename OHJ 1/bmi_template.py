"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 050282836
Name:       Pyry Laine
Email:      pyry.j.laine@tuni.fi

BMI- counter
"""


from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        paino = Label(self.__mainwindow, text= "paino (kg):")
        paino.pack()

        self.__weight_value = Entry(self.__mainwindow)
        self.__weight_value.pack()

        # TODO: Create an Entry-component for the height.
        pituus = Label(self.__mainwindow, text="pituus (cm):")
        pituus.pack()

        self.__height_value = Entry(self.__mainwindow)
        self.__height_value.pack()

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text= "calculate", command= self.calculate_BMI)
        self.__calculate_button.pack()

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="")
        self.__result_text.pack()

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow)
        self.__explanation_text.pack()

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text= "stop", command= self.stop)
        self.__stop_button.pack()


    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            paino = float(self.__weight_value.get())
            pituus = float(self.__height_value.get())
            BMI = float(paino/pituus**2)*10000

            if paino >= 0 and pituus >= 0:
                self.__result_text.config(text= f"{BMI:.2f}")

                if BMI < 18.5:
                    self.__explanation_text.config(text= "You are underweight.")

                elif BMI > 25:
                    self.__explanation_text.config(text="You are overweight.")

                else:
                    self.__explanation_text.config(text="Your weight is normal.")

            else:

                self.__explanation_text.config(text= "Error: height and weight must be positive.")
                self.reset_fields()
        except ValueError:

            self.__explanation_text.config(text= "Error: height and weight must be numbers.")
            self.reset_fields()

    # TODO: Implement this method.

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.config(text= "")
        self.__weight_value.delete(0, END)
        self.__height_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
