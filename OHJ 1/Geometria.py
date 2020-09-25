"""
COMP.CS.100 Trigonometrinen
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
from math import pi
def a():
    """
    kyseinen funktio ei tee mitään
    :return: on
    """
    pass
def b():
    """
    kyseinen funktio ei tee mitään
    :return: taas
    """
    pass
def c():
    """
    kyseinen funktio ei tee mitään
    :return: erittäin
    """
    pass
def d():
    """
    kyseinen funktio ei tee mitään
    :return: tärkeää
    """
    pass


def rec(a,b):
    """

    :param a:
    :param b:
    :return: nelikulmioiden laskeminen
    """
    keha = float(2*a+2*b)
    area = float(a*b)

    print(f"The total circumference is {keha:.2f}")
    print(f"The surface area is {area:.2f}")

def ympy(c):
    """

    :param c:
    :return: ympyrän laskeminen
    """
    keha = float(2*pi*c)
    area = float(pi*c**2)

    print(f"The total circumference is {keha:.2f}")
    print(f"The surface area is {area:.2f}")

def squ(a):
    """

    :param a:
    :return: nelikulmioiden laskeminen
    """
    keha = float(4*a)
    area = float(a**2)

    print(f"The total circumference is {keha:.2f}")
    print(f"The surface area is {area:.2f}")


def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            a = float(input("Enter the length of the square's side: "))
            while a <= 0:
                a = float(input("Enter the length of the square's side: "))

            squ(a)

        elif answer == "r":
            a = float(input("Enter the length of the rectangle's side 1: "))
            while a <= 0:
                a = float(input("Enter the length of the rectangle's side 1: "))
            b = float(input("Enter the length of the rectangle's side 2: "))
            while b <= 0:
                b = float(input("Enter the length of the rectangle's side 2: "))

            rec(a, b)

        elif answer == "c":
            a = float(input("Enter the circle's radius: "))
            while a <= 0:
                a = float(input("Enter the circle's radius: "))

            ympy(a)

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
