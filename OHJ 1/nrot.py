"""
COMP.CS.100 nrot2
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def main():
    nrot = []
    print("Give 5 numbers:")
    for i in range(0,5):
        a = int(input("Next number: "))
        nrot.append(a)

    print("The numbers you entered, in reverse order:")
    nrot.reverse()
    for o in range(0,5):
        print(str(nrot[o]))

if __name__ == "__main__":
    main()
