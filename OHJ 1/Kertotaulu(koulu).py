# COMP.CS.100 kertokoulu
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

nro = int(input('Choose a number: '))

def main(nro):
    sarja = 1
    if nro <= 6:
        while sarja * nro <= 104:
            vast = int(sarja * nro)
            print(sarja, "*", nro,'=', vast)
            sarja +=1
    elif nro > 6:
        while sarja * nro <= 110:
            vast = int(sarja * nro)
            print(sarja, "*", nro,'=', vast)
            sarja +=1

if __name__ == '__main__':
    main(nro)