"""
COMP.CS.100 genre
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    Ottaa sisäänsä tiedoston nimen ja palauttaa
    """

    sanakirja = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for genre in genres:


                if genre in sanakirja:
                    sanakirja[genre].append(name)
                else:
                    sanakirja[genre] = [name]

        file.close()
        return sanakirja

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    kategoriat = sorted(genre_data)

    stri = ", ".join(kategoriat)
    print(f"Available genres are: {stri}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return
        elif genre not in kategoriat:
            pass
        else:
            arvo = genre_data[genre]
            for i in sorted(arvo):
                print(i)
            pass

        # TODO print the series belonging to a genre.


if __name__ == "__main__":
    main()