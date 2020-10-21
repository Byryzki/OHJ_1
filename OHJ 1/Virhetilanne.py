"""
COMP.CS.100 Virhetilanne
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def print_box(w, h, m):
    """varsinainen toiminto"""
    for i in range(0, h):
        print(m*w)

def read_input(value):
    """Tarkistaa, että syöte on positiivisia kokonaislukuja"""
    while True:
        try:
            arvo = int(input(value))
            while arvo <= 0:
                arvo = (input(value))
                break
            return arvo


        except ValueError:
            pass

def main():
    """Säilöö ohjelman parametrit ja toteutus"""
    w = read_input("Enter the width of a frame: ")
    h = read_input("Enter the height of a frame: ")
    m = input("Enter a print mark: ")
    print()
    print_box(w, h, m)



if __name__ == "__main__":
    main()