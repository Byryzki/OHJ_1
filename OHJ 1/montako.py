"""
COMP.CS.100 montako löytyy
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

def input_to_list(nro):
    """ tämä funktio tekee kaikkee kivaa"""
    nrot = []
    print(f"Enter {nro} numbers:")
    for i in range(0, nro):
        x = int(input(""))
        nrot.append(x)

    haku = int(input("Enter the number to be searched: "))
    y = nrot.count(haku)

    if y > 0:
        print(f"{haku} shows up {y} times among the numbers you have entered.")
    elif y <= 0:
        print(f"{haku} is not among the numbers you have entered.")


def main():
    nro = int(input("How many numbers do you want to process: "))
    input_to_list(nro)


if __name__ == "__main__":
    main()