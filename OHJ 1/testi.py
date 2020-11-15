luvut = open("murto", "r")
t = []
nimi = []
eka = []
toka = []
for rivi in luvut:
    nimi = rivi[0]
    a = int(rivi[2])
    b = int(rivi[4])
    print(nimi, a, b)
    #murtod[nimi] = (Fraction(a, b))
