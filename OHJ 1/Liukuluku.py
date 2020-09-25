"""
COMP.CS.100 Parasetamoli
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

def compare_floats(eka, toka, EPS):
    if abs(eka - toka) < EPS:
        return True

    elif abs(eka - toka) >= EPS:
        return False


def main():
    eka = float(input(""))
    toka = float(input(""))
    EPS = float(input(""))

    compare_floats(eka, toka, EPS)
    print(compare_floats(eka, toka, EPS))


if __name__ == "__main__":
    main()