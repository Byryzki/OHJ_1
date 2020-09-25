"""
COMP.CS.100 MC Donald
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

"""
Old Mc Donald had a farm -laulun sanat 
"""
def print_verse(a, s):
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {a}")
    print("E-I-E-I-O")
    print(f"With a {s} {s} here")
    print(f"And a {s} {s} there")
    print(f"Here a {s}, there a {s}")
    print(f"Everywhere a {s} {s}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()

"""
Laulun säkeistöjen parametrit eläimelle ja äänteelle
"""
def main():
    a = "cow"
    s = "moo"
    print_verse(a, s)

    a = "pig"
    s = "oink"
    print_verse(a, s)

    a = "duck"
    s = "quack"
    print_verse(a, s)

    a = "horse"
    s = "neigh"
    print_verse(a, s)

    a = "lamb"
    s = "baa"
    print_verse(a, s)



if __name__ == "__main__":
    main()

