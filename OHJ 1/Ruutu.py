"""
COMP.CS.100 Yogi Bear
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

"""
Tämä funktio hoitaa päätehtävän, eli kuvion muodostamisen
"""
def print_box(w, h, m):

    for i in range(0, h):
        print(m*w)

"""
Tähän funktioon varastoidaan parametrit
"""
def main():
    w = int(input("Enter the width of a frame: "))
    h = int(input("Enter the height of a frame: "))
    m = input("Enter a print mark: ")

    print()
    print_box(w, h, m)


if __name__ == "__main__":
    main()