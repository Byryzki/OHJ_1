"""
COMP.CS.100 Lotto
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
from math import factorial as ft

def positive(ball, drawn):
    """

    :param ball: alkeistapaukset
    :param drawn: suotuisat tapaukset
    :return: huolehtii, että syöte määrittelyjoukossa
    """
    if ball <= 0:
        print("The number of balls must be a positive number.")
    elif drawn > ball:
        print("At most the total number of balls can be drawn.")
    else:
        calc(ball, drawn)

def calc(ball, drawn):
    """

    :param ball: vaihtoehtojen määrä
    :param drawn: suotuisat tapaukset
    :return: laskee todennäköisyyden ja näyttää sen ulostuloon
    """
    prob = int((ft(ball) / (ft(drawn)*ft(ball - drawn))))
    return print(f"The probability of guessing all {drawn} balls correctly is 1/{prob}")


def main():
    ball = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))
    positive(ball, drawn)

if __name__ == "__main__":
    main()