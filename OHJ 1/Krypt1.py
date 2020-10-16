"""
COMP.CS.100 ROT-13-salaus
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

def row_encryption(viesti):
    """
    :param viesti: syötetty merkkijono
    :return: kyrptattu merkkijono
    """
    perus = []
    krypt = []

    for i in viesti:
        perus.append(i)

    for i in perus:
        krypt.append(encrypt(i))

    #merkkijonoon lisäys
    valmis = ""
    for i in krypt:
        valmis += i

    return valmis

def main():
    viesti = input("kerro viestisi: ")
    row_encryption(viesti)

if __name__ == "__main__":
    main()