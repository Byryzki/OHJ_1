"""
COMP.CS.100 accesscontrol- projekti
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}

class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Määrittelee luokan parametrit ja kulkuoikeudet listaksi

        :param id: str, kortin omistajan ID
        :param name: str, kortin omistajan nimi
        """

        self.__id = id
        self.__name = name
        self.__access = []

    def info(self):
        """
        Metodin tehtävänä palauttaa mainille tiedot luokalta:
        id, name, access: a1,a2,...
        Esimerkki:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Itse tulostus tehdään main-funktiossa.
        """
        pilkutus = ", "
        paasyt = sorted(self.__access)

        return f"{self.__id}, {self.__name}, access: {', '.join(paasyt)}"

    def get_name(self):
        """
        :return: Antaa mainille kulkuluvan omistajan nimen.
        """

        return f"{self.__name}"


    def add_access(self, new_access_code):
        """
        Lisää uuden kulkuluvan access listaan, jos ei jo ole siellä.

        :param new_access_code: uusi kulkulupa
        """
        uusik = list(new_access_code.split(" "))

        if any(item in uusik for item in self.__access): #jos kulku jo entuudestaan
            pass

        else:
            self.__access.extend(uusik)
            self.__access.sort()


    def check_access(self, door):
        """
        Tarkastaa, onko henkilöllä kulkuoikeus kyseisestä ovesta.

        :param door: str, ovi, josta kysytään kulkuoikeutta.
        :return: True: Ovi avautuu kulkukortilla.
                 False: Ovi ei avaudu kulkukortilla.
        """
        dooraccess = []
        dooraccess.extend(DOORCODES[door])
        dooraccess.append(door)

        if DOORCODES[door] != []:
            check = any(item in dooraccess for item in self.__access)
            if check is True:
                return True
            else:
                return False

        else:
            if door in self.__access:
                return True
            else:
                return False
        pass

    def merge(self, card):
        """
        Lisätään halutut kulkuoikeudet toiseen korttiin.
        :param card: Kortti mistä oikeudet liitetään tähän korttiin.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        self.__access.extend(card.__access)

        uusi = list(dict.fromkeys(self.__access))
        self.__access.sort()
        self.__access = uusi

        pass

    def remove_duplicates(self):
        """
        Jos sama kulkuoikeus moneen kertaan, poistaa nämä.

        :return:
        """
        for i in self.__access:
            for koodi, alue in DOORCODES.items():
                if i in alue and koodi in self.__access:
                    self.__access.remove(koodi)

        res = []
        for i in self.__access:
            if i not in res:
                res.append(i)

        self.__access = res

def main():
    """
    Kaksi dictionaryä. Dictiin saadaan tallennettua avaimeksi ID
    ja valueksi pääsyoikeudet listana.
     Dict2 saadaan tallennettua avaimeksi ID ja valueksi ID:tä vastaava olio.
    """
    dict = {}
    dict2 = {}

    file = open('accessinfo.txt', mode='r')

    for row in file:
        id, name, access = row.rstrip().split(";")
        oikeudet = list(access.split(","))
        dict2[id] = Accesscard(id, name)
        dict[id] = oikeudet

    for i in dict2:
        str1 = " ".join(dict[i])
        dict2[i].add_access(str1)
    """Ohjelman käyttö osio"""

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            """Listaa kaikkien henkilöiden tiedot"""
            for key in sorted(dict2):
                dict2[key].remove_duplicates()
                print(dict2[key].info())
            pass

        elif command == "info" and len(strings) == 2:
            """
            Kertoo yksittäistä ID:tä vastaavat tiedot
            Jos ID kirjoitettu väärin tai sitä ei ole olemassa annetaan error.
            """
            try:
                card_id = strings[1]
                dict2[card_id].remove_duplicates()
                print(dict2[card_id].info())
            except KeyError:
                print("Error: unknown id.")
            pass

        elif command == "access" and len(strings) == 3:
            """
            Kertoo onko ID:llä oikeus päästä ovesta.
            Jos ID tai ovi kirjoitettu väärin tai sitä ei ole: error.
            """
            card_id = strings[1]
            door_id = strings[2]

            if card_id not in dict2:
                print("Error: unknown id.")

            elif door_id not in DOORCODES:
                print("Error: unknown doorcode.")

            elif dict2[card_id].check_access(door_id):
                print(f"Card {card_id} ( {dict2[card_id].get_name()} ) has access to door {door_id}")

            else:
                print(f"Card {card_id} ( {dict2[card_id].get_name()} ) has no access to door {door_id}")

            pass

        elif command == "add" and len(strings) == 3:
            """
            Voidaan syöttää henkilölle lisää kulkuoikeuksia kunhan ID ja pääsykoodi kirjoitettu oikein
            """

            card_id = strings[1]
            access_code = list(strings[2].split(" "))

            if card_id not in dict2:
                print("Error: unknown id.")

            elif strings[2] not in DOORCODES.keys() and access_code not in DOORCODES.values():
                print("Error: unknown accesscode.")

            else:
                dict2[card_id].add_access(strings[2])

            pass

        elif command == "merge" and len(strings) == 3:
            """
            Kopioi toisen henkilön kulkuoikeudet toiselle henkilölle.
            Antaa error jos toinen ID on väärin tai sitä ei ole olemassa.
            """
            card_id_to = strings[1]
            card_id_from = strings[2]

            if card_id_to not in dict2 or card_id_from not in dict2:
                print("Error: unknown id.")

            else:
                dict2[card_id_to].merge(dict2[card_id_from])
            pass

        elif command == "quit":
            """Ohjelman lopetus"""
            print("Bye!")
            return

        else:
            print("Error: unknown command.")



if __name__ == "__main__":
    main()
