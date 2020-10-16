"""
COMP.CS.100 ROT-13 c
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def encrypt(merkki):
    """
    :param merkki: 1 syötetty merkki
    :return: 1 kryptattu merkki
    """
    #normaalien kirjainten listaaminen
    a = "abcdefghijklmnopqrstuvwxyz"
    A = a.upper()
    b = a + A
    norm = []
    for i in range(0, len(b)):
        norm.append(b[i])

    # kryptattujen kirjainten listaaminen
    k = "nopqrstuvwxyzabcdefghijklm"
    K = k.upper()
    s = k + K
    krypt = []
    for i in range(0, len(s)):
        krypt.append(s[i])

    if merkki in norm:
        # selvitetään syötteen indeksi
        ind = norm.index(merkki)
        return krypt[ind] #käännetty merkki
    elif merkki not in norm:
        return merkki

def row_encryption(row):
    """

    :param row: syötetty merkkijono
    välissä lähettää merkki kerrallaan encrypt
    :return: kyrptattu merkkijono
    """
    perus = []
    krypt = []

    for i in row:
        perus.append(i)

    for i in perus:
        krypt.append(encrypt(i))

    #merkkijonoon lisäys
    valmis = ""
    for i in krypt:
        valmis += i

    return valmis


def read_message():
    """
    tekee syötetyn tekstin
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

    for i in range(0, len(rows)):
        row_encryption(rows[i])

    valmislist = []
    for i in range(0, len(rows)):
        valmislist.append(row_encryption(rows[i]))

    print("ROT13:")
    for row in valmislist:  # listasta merkkijonoksi
        "".join(row)
        print(row)

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")

    msg = read_message()
    valmis = ""


if __name__ == "__main__":
    main()