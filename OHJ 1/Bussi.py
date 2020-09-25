"""
COMP.CS.100 bussi
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def aikataulu(kello):
    """ laskee seuraavat 3 lähintä bussintuloaikaa"""
    ajat = [630, 1015, 1415, 1620, 1720, 2000]
    print("The next buses leave:")
    if kello <= ajat[-3]:
        ajat.append(kello)
        ajat.sort()

        print(ajat[(ajat.index(kello)) + 1])
        print(ajat[(ajat.index(kello)) + 2])
        print(ajat[(ajat.index(kello)) + 3])
    elif kello > ajat[-3] and kello <= ajat[-2]:
        print(ajat[-2])
        print(ajat[-1])
        print(ajat[0])
    elif kello > ajat[-2] and kello <= ajat[-1]:
        print(ajat[-1])
        print(ajat[0])
        print(ajat[1])
    elif kello > ajat[-1]:
        print(ajat[0])
        print(ajat[1])
        print(ajat[2])



def main():
    kello = int(input("Enter the time (as an integer): "))
    aikataulu(kello)

if __name__ == "__main__":
    main()