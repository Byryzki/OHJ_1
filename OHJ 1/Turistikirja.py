"""
COMP.CS.100 turistisanakirja
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def main():
    english_spanish = {"hey": "hola",
                       "thanks": "gracias",
                       "home": "casa"}

    print("Dictionary contents:")
    dict = []
    for key in english_spanish:
        dict.append(key)

    print(str(", ".join(sorted(dict))))  # lista str:ksi

    while True:
        spaeng = {v: k for k, v in english_spanish.items()}
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng = str(input("Give the word to be added in English: "))
            spa = str(input("Give the word to be added in Spanish: "))

            english_spanish[eng] = spa

            print("Dictionary contents:")
            dict = []
            for key in english_spanish:
                dict.append(key)

            print(str(", ".join(sorted(dict))))  # lista str:ksi

        elif command == "R":
            pois = input("Give the word to be removed: ")

            if pois in english_spanish:
                del english_spanish[pois]
            else:
                print(f"The word {pois} could not be found from the dictionary.")

        elif command == "P":
            print("English-Spanish")
            for key, value in sorted(english_spanish.items()): #tulosta dict aakkosjärj.
                print(key, value)
            print()
            print("Spanish-English")
            for key, value in sorted(spaeng.items()):  # tulosta dict aakkosjärj.
                print(key, value)

        elif command == "T":
            uusi = ""
            usi = []
            text = input("Enter the text to be translated into Spanish: ")
            text = text.split(" ")
            print("The text, translated by the dictionary:")
            for i in range(len(text)):
                if text[i] in english_spanish:
                    a = english_spanish[text[i]]
                    usi.append(a)
                elif text[i] not in english_spanish:
                    usi.append(text[i])

            print(str(" ".join(usi))) #lista str:ksi
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
