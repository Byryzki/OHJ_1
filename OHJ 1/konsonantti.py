"""
COMP.CS.100 konsonantti
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def laskin(sana):
    """

    :param sana: syötetty sana
    :return:  montako mitäkin
    """
    vokaalit = ["a","e","i","o","u","ä","ö"]
    v= 0
    k= 0
    for i in range(0, len(sana)):
        if sana[i] in vokaalit:
            v+= 1
        else:
            k+= 1

    print(f"The word {sana} contains {v} vowels and {k} consonants")

def main():
    sana = str(input("Enter a word: "))
    laskin(sana)

if __name__ == "__main__":
    main()