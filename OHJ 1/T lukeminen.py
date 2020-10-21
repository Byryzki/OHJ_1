"""
COMP.CS.100 kehittynyt booboo
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def main():
    nimi = input("Enter the name of the file: ")
    luku = 1
    try:
        boo = open(nimi, mode="w")

    except OSError:
        print(f"Writing the file {nimi} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    try:
        while True:
            rivi = input()

            if rivi == "":
                break

            valmis = str(f"{luku} {rivi}")
            print(valmis, file= boo)
            luku +=1

    except OSError:
        print(f"Writing the file {nimi} was not successful.")
        return

    print(f"File {nimi} has been written.")


if __name__ == "__main__":
    main()
