"""
COMP.CS.100 sanantheys
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    rivit = [] # rivit
    sanat = [] # sanat yksittäin
    dict = {}
    while True:
        rivi = input("")
        rivit.append(rivi.split(" "))
        if rivi == "":
            break #input rivit

    for lista in rivit: #listat listaksi
        for sana in lista:
            sanat.append(sana.lower())
    sanat.pop()

    for sana in sanat: # sanat ja niiden määrät dict:iin
        dict[sana] = sanat.count(sana)


    for key, value in sorted(dict.items()): # dict (key:value) tulostus pystyssä aakkosjärjestyksessä
        print(f"{key} : {value} times")


if __name__ == "__main__":
    main()