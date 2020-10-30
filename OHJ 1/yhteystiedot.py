"""
COMP.CS.100 yhteystiedot
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def read_file(filename):
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

        return info
    except:
        return


def main():
    filename = input()
    read_file(filename)

if __name__ == "__main__":
    main()