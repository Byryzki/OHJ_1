"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
# a) Implement the class Player here.
class Player:
    def __init__(self, inturn):
        points = 0
        heitot = 0
        osumat = 0
        prosentti = 0

        self.__inturn = inturn
        self.__points = points
        self.__heitot = heitot
        self.__osumat = osumat
        self.__prosentti = prosentti


    def get_name(self):

        return self.__inturn

    def get_points(self):
        points = self.__points
        return points

    def varoitus(self):
        points = self.__points

        if 40 <= self.__points and self.__points <= 49:
            print(f"{self.__inturn} needs only {str(50-self.__points)} points. It's better to avoid knocking down the pins with higher points.")

    def has_won(self):
        if self.__points == 50:
            return True

    def heitot(self):
        self.__heitot += 1

    def huuto(self, pts):
        if self.__points <= 50:

            ka = self.__points / self.__heitot

            if pts > ka:
                print(f"Cheers {self.__inturn}!")
        else:
            return


    def osumat(self, pts):
        if pts > 0:
            self.__osumat += 1

    def hs(self):
        if self.__heitot == 0:
            self.__prosentti = 0.0
            return self.__prosentti
        else:
            self.__prosentti = (self.__osumat / self.__heitot) * 100
            return self.__prosentti

    def add_points(self, pts):
        totuus = True

        self.__points = self.__points + pts

        if self.__points > 50:
            print(f"{self.__inturn} gets penalty points!")
            self.__points = 25
            totuus = False

        points = self.__points
        if points >= 40 and points <=49:
            print(f"{self.__inturn} needs only {str(50-self.__points)} points. It's better to avoid knocking down the pins with higher points.")
            if totuus:
                try:
                    ka = self.__points / self.__heitot
                    if pts > ka:
                        print(f"Cheers {self.__inturn}!")
                except ZeroDivisionError:
                    return

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1

    while True:
        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1
            player1.heitot()

        # else throw is an odd number
        else:
            in_turn = player2
            player2.heitot()

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.osumat(pts)
        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        in_turn.huuto(pts)

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.hs():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.hs():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
