"""
COMP.CS.100 KOlmion ala
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

from math import sqrt

def area(a,b,c):
    s = ((a+b+c)/2)
    x = (sqrt(s*(s-a)*(s-b)*(s-c)))
    return x

def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    x = area(a,b,c)
    print(f"The triangle's area is {x:.1f}")


if __name__ == "__main__":
    main()