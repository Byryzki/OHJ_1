# COMP.CS.100 onko tylsää virhe
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

def main():
    x = input("Bored? (y/n) ")
    if x == 'Y' or x == 'y':
        print("Well, let's stop this, then.")

    elif x == 'N' or x == 'n':
        while x == 'n' or x== 'N':
            x = input("Bored? (y/n) ")

            if x == 'Y' or x == 'y':
                print("Well, let's stop this, then.")

    else:
        while x != 'Y' and x != 'y' and x != 'N' and x != 'n':

            print("Incorrect entry.")
            x = input('Please retry: ')

            if x == 'Y' or x == 'y':
                print("Well, let's stop this, then.")

            elif x == 'N' or x == 'n':
                while x == 'n' or x == 'N':
                    x = input("Bored? (y/n) ")

                    if x == 'Y' or x == 'y':
                        print("Well, let's stop this, then.")

if __name__ == '__main__':
    main()