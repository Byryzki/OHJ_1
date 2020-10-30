"""
COMP.CS.100 yhteystiedot
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def read_file(filename="contacts.csv", k="Mike", val="skype"):
    """ öd vlloks vö  bfö bäv"""
    info = {}
    try:
        file = open(filename, mode="r")


        for row in file:
            key, name, phone, email, skype = row.rstrip().split(";")
            info[key] = {'name': name,
                         'phone': phone,
                         'email': email,
                         'skype': skype}

        return print(info[k][val])

    except:
        return
read_file()