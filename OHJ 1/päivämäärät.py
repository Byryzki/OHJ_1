# COMP.CS.100 päivämäärät (vuosi)
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

def main():
    p = 1
    k = 1
    q = 5

    for i in range(0,12):
        if k == 6 or k == 9 or k == 11 or k == 4:
            for j in range(0,30):
                print(p, ".", k,".", sep="")
                p+= 1

        elif k == 2:
            for j in range(0,28):
                print(p, ".", k, ".", sep="")
                p+= 1

        else:
            for j in range(0,31):
                print(p, ".", k, ".", sep="")
                p+= 1

        p= 1
        k+= 1

if __name__ =="__main__":
    main()