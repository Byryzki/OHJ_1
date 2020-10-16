"""
COMP.CS.100 hintalista
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    while True:
        tuote = input("Enter product name: ")
        tuote = tuote.replace(" ", "")
        if tuote == "" or tuote == len(tuote) * " ":
            print("Bye!")
            break

        elif tuote not in PRICES:
            print(f"Error: {tuote} is unknown.")
        elif tuote in PRICES:
            print(f"The price of {tuote} is {PRICES[tuote]:.2f} e")




if __name__ == "__main__":
    main()
