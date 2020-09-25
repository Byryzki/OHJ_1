"""
COMP.CS.100 Tikkupeli
Tekijä: Pyry Laine ja Mikko Kiviniemi
Opiskelijanumeroni: 050282836

Peli imitoi legendaarista tikkupeliä, jossa kaksi pelaajaa poistaa vuorotellen tikkuja kasasta 1-3 kappaletta ja se, joka siirtää viimeisen tikun häviää.
"""

def main():
    # aloitus ja muuttujat
    print("Game of sticks")
    sticks = 21
    turn = 1
    #varsinainen pelin kierto
    while sticks > 0:
        #pelaaja 1 vuorolla:
        if turn % 2 != 0 and sticks > 0:
            p1 = int(input("Player 1 enter how many sticks to remove: "))
            if p1 == 1 or p1 == 2 or p1 == 3:
                turn +=1
                sticks -= p1
                if sticks > 0:
                    print("There are", sticks, "sticks left")
            elif p1 != 1 or p1 != 2 or p1 != 3:
                print("Must remove between 1-3 sticks!")
        # pelaaja 2 vuorolla:
        elif turn % 2 == 0 and sticks > 0:
            p2 = int(input("Player 2 enter how many sticks to remove: "))
            if p2 == 1 or p2 == 2 or p2 == 3:
                turn += 1
                sticks -= p2
                if sticks > 0:
                    print("There are", sticks, "sticks left")
            elif p2 != 1 or p2 != 2 or p2 != 3:
                print("Must remove between 1-3 sticks!")


        #tikkujen loputtua:
        elif sticks <= 0:
            break

    #pelin lopetus
    if turn % 2 == 0:
        print("Player 1 lost the game!")

    elif turn % 2 != 0:
        print("Player 2 lost the game!")

if __name__ == "__main__":
    main()