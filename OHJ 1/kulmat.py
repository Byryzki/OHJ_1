"""
COMP.CS.100 Kulmat
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def calculate_angle(e, t = int(90)):
    """
    :param e: ensimmäinen kulma
    :param t: toinen kulma
    :return: Laskee ja palauttaa oikean 3. kulman arvon
    """
    x = 180-t-e

    return x

def main():
    e = int(input("syötä 1. kulma: "))
    t = int(input("syötä 2. kulma: "))

    calculate_angle(e, t)

    print(int(calculate_angle(e, t)))

if __name__ == "__main__":
    main()