"""
COMP.CS.100 pisteiden laskentaa
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def main():
    piste = input("Enter the name of the score file: ")
    tulokset = {}

    try:
        tulos = open(piste, "r")
    except OSError:
        print("There was an error in reading the file.")
        return

    for rivi in tulos:
        try:
            (key, val) = rivi.split(" ")
        except ValueError:
            print("There was an erroneous line in the file:")
            print(rivi)
            return

        try:
            val = int(val)

            if key in tulokset:
                tulokset[key] += val
            else:
                tulokset[key] = val
        except ValueError:
            print("There was an erroneous score in the file:")
            print(val)
            return

    print("Contestant score:")
    for i in sorted(tulokset):
        print(i, tulokset[i])

    tulos.close()

if __name__ == "__main__":
    main()
