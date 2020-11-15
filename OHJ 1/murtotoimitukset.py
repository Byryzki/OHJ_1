"""
COMP.CS.100 murtotoimitukset
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator
        self.__value = numerator / denominator

    def __str__(self):
        teksti = f"{self.__numerator}/{self.__denominator}"
        return teksti

    def __lt__(self, frac2):
        self.__value = self.__numerator/self.__denominator
        frac2.__value = frac2.__numerator/frac2.__denominator
        if self.__value < frac2.__value:
            return True
        else:
            return False

    def __gt__(self, frac2):
        self.__value = self.__numerator / self.__denominator
        frac2.__value = frac2.__numerator / frac2.__denominator
        if self.__value > frac2.__value:
            return True
        else:
            return False

    def simplify(self):
        """ sieventää murtolukua suurimmalla yhteisellä tekijällä """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)

        self.__numerator = int(self.__numerator / gcd)
        self.__denominator = int(self.__denominator / gcd)

        self.return_string()
        return f"{self.__numerator}/{self.__denominator}"


    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"



    def completent(self):
        return Fraction(-1*self.__numerator, self.__denominator)

    def reciprocal(self):
        oso = self.__numerator
        nim = self.__denominator

        self.__numerator = nim
        self.__denominator = oso

        return Fraction(self.__numerator, self.__denominator)

    def multiply(self, frac2):
        a = self.__numerator * frac2.__numerator
        b = self.__denominator * frac2.__denominator

        return Fraction(a, b)

    def divide(self, frac2):

        yla = self.__numerator
        ala = self.__denominator

        self.__numerator = ala
        self.__denominator = yla

        self.__numerator = self.__numerator * frac2.__numerator
        self.__denominator = self.__denominator * frac2.__denominator

        return Fraction(self.__denominator, self.__numerator)


    def add(self, frac2):

        ala1 = self.__denominator * frac2.__denominator
        yla1 = self.__numerator * frac2.__denominator

        yla2 = self.__denominator * frac2.__numerator

        ylav = yla1 + yla2

        self.__numerator = ylav
        self.__denominator = ala1

        return Fraction(self.__numerator,self.__denominator)


    def deduct(self, frac2):
        ala1 = self.__denominator * frac2.__denominator
        yla1 = self.__numerator * frac2.__denominator

        yla2 = self.__denominator * frac2.__numerator

        ylav = yla1 - yla2

        self.__numerator = ylav
        self.__denominator = ala1

        return Fraction(self.__numerator, self.__denominator)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    murtod = {}
    while True:
        comm = input("> ")
        if comm == "add":
            luku = input("Enter a fraction in the form integer/integer: ")
            nimi = input("Enter a name: ")
            nrot = luku.split("/")
            a = int(nrot[0])
            b = int(nrot[1])
            murtod[nimi] = (Fraction(a, b))

        elif comm == "print":
            haku = input("Enter a name: ")
            if haku in murtod:
                print(f"{haku} = {murtod[haku]}")
            else:
                print(f"Name {haku} was not found")

        elif comm == "list":
            for key, value in sorted(murtod.items()):
                print(f"{key} = {value}")

        elif comm == "*":
            eka = input("1st operand: ")
            if eka not in murtod:
                print(f"Name {eka} was not found")

            else:
                toka = input("2nd operand: ")
                if toka not in murtod:
                    print(f"Name {toka} was not found")

                else:
                    eka = murtod[eka]
                    toka = murtod[toka]

                    print(f"{eka.return_string()} * {toka.return_string()} = {eka.multiply(toka)}")
                    print(f"simplified {(eka.multiply(toka)).simplify()}")

        elif comm == "file":
            fnimi = input("Enter the name of the file: ")
            try:
                luvut = open(fnimi, "r")

                for rivi in luvut:
                    nimi = rivi[0]
                    a = int(rivi[2])
                    b = int(rivi[4])
                    murtod[nimi] = (Fraction(a, b))
            except:
                print("Error: the file cannot be read.")

        elif comm == "quit":
            print("Bye bye!")
            break

        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()