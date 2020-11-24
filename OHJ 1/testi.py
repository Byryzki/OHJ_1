dict = {}

nimi = "accessinfo.txt"
file = open(nimi, "r")

for rivi in file:
    id, name, access = rivi.split(";")
    dict[id] = name, access

tieto = list(dict.values())[0]

print(tieto[0])