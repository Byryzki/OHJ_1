"""
COMP.CS.100 konsonantti
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def read_message():
    """

    :return: lista syötteistä
    """
    rows = []
    on = True
    while on == True:
        msg = str(input())
        rows.append(msg)
        if msg == "":
            on = False

    rows.pop() #poistetaan tyhjä m.jono
    return rows

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")

    msg = read_message()
    valmis = ""

    print("The same, shouting:")
    for row in msg: #listasta merkkijonoksi
        "".join(row)
        print(row.upper())

if __name__ == "__main__":
    main()
