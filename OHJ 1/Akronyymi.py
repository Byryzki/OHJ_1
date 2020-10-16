"""
COMP.CS.100 Nimikääntäjä
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def create_an_acronym(sana):
    """

    :param sana: wegrhj
    :return: wdfgfderg
    """
    sana.split()
    list = []
    for i in range(0, len(sana)):
        if i == 0:
            list.append(sana[i])
        elif sana[i] == " ":
            list.append(sana[i+1])
        else:
            pass

    vittu = "".join(list)
    return vittu.upper()


def main():
    sana = str(input("anna sana: "))
    create_an_acronym(sana)

if __name__ == "__main__":
    main()