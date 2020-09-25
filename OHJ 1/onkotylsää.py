# COMP.CS.100 onko tylsää
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

def main():
    x = ""
    while x == 'n' or 'N':
        x = input("Bored? (y/n) ")

        if x == "y" or 'Y':
            print("Well, let's stop this, then.")
        elif x != "y" or x != "Y" or x!= "n" or x!= "N":
            print("Incorrect entry")

if __name__ == '__main__':
  main()
