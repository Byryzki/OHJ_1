"""
COMP.CS.100 tanssipeli
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

def main():
    PRICES = {
        "milk": 1.09, "fish": 4.56, "bread": 2.10,
        "chocolate": 2.70, "grasshopper": 13.25,
        "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
        "bananas": 1.05, "Pepsi": 3.15, "pizza": 4.15,
    }
    def maara(key):
        return PRICES[key]

    for tuote, value in sorted(PRICES.items(), key=lambda x: x[1]):
        print(f"{tuote} {PRICES[tuote]:.2f}")

if __name__ == "__main__":
    main()
