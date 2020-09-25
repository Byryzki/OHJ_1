"""
COMP.CS.100 suuruus
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def kubiikki(x):
    """

    :param x: jotain
    :return: jotain jotain
    """
    x.remove(min(x))
    x.remove(max(x))

    kesk = ((x[0] + x[1] + x[2]) / 3)
    print(f"The official competition score is {kesk:.2f} seconds.")


def main():
    x = []
    for i in range(0,5):
        tulos = float(input(f"Enter the time for performance {i+1}: "))
        x.append(tulos)

    kubiikki(x)


if __name__ == "__main__":
    main()