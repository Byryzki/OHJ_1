"""
COMP.CS.100 Nimikääntäjä
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def reverse_name(nimi):
    """
    :param nimi: syötetty nimi
    :return:  käännetty
    """
    x= 0
    if "," in nimi:
        for i in range(0, len(nimi)):
            if nimi[i] == ",":
                x = i+1
            else:
                pass
    elif "," not in nimi:
        pass

    suku = str(nimi[0:x])
    etu = str(nimi[x: len(nimi)])

    if etu == "" or suku == "" or etu == "," or suku == ",":
        koko = f"{etu.strip(' ,')}{suku.strip(' ,')}"
    else:
        koko = f"{etu.strip(' ,')} {suku.strip(' ,')}"

    return koko

def main():
    nimi = str(input(""))
    reverse_name(nimi)

if __name__ == "__main__":
    main()