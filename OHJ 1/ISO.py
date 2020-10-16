"""
COMP.CS.100 ISO kirjain
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def capitalize_initial_letters(sana):
    """
    :param sana: wegrhj
    :return: wdfgfderg
    """
    sana.lower()
    list = []
    for i in range(0, len(sana)):
        if i == 0:
            list.append(sana[i].upper())
        elif sana[i-1] == " ":
            list.append(sana[i].upper())
        else:
            list.append(sana[i].lower())

    x = "".join(list)
    return x

def main():
    sana = str(input("anna sana: "))
    capitalize_initial_letters(sana)

if __name__ == "__main__":
    main()