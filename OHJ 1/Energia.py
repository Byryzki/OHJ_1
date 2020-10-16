"""
COMP.CS.100 Nimikääntäjä
Tekijä: Pyry Laine ja Mikko Kiviniemi
Opiskelijanumeroni: 050282836 ja H292652
"""


def print_single_histogram_line(arvot):
    sorted(arvot)
    print("0-9: ")
    for i in range(1, len(max(arvot))):
        print("1", i * "0", "-", (i+1) * "9", ": ", sep="")

def tahti(arvot):
    #luokitus
    #jarvot = sorted(arvot) #syötetyt arvot järjestyksessä
    luokat = []
    montako = []

    for i in range(0, len(arvot)):
        pituus = len(arvot[i])
        luokat.append(pituus)
        montako.append(luokat.count(i))

    print(luokat)



def main():
    arvot = []
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()
    x = True
    while x == True:
        vastaus = input("Enter energy consumption (kWh): ")
        if vastaus == "":
            x = False
            print_single_histogram_line(arvot)
            tahti(arvot)

        elif int(vastaus) < 0:
            print(f"You entered: {vastaus}, Enter non-negative numbers only!")
        elif int(vastaus) >= 0:
            arvot.append(vastaus)


if __name__ == "__main__":
    main()