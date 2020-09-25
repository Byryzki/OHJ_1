#TERMISTÖ
'''
#string (str): pelkkää tekstiä
#variable (var): muuttuja
#boolean : tosi tai epätosi
#float : reaaliluvut
#integer (int): kokonaisluku
#function (func): pala koodia, joka tekee tietyn tehtävä
#parameter : funktiossa käytettävä muuttuja
#none : funktiota ei ole pyydetty palauttamaan arvoa
'''
#MUUTTUJAT JA DATATYYPIT
character_age = "31.530"
character_name = "pekka"
print(character_name)
print('olipa kerran ' + character_name + ', joka oli ' + character_age + ' vuotias')

character_name = "mika"
print(character_name)

#TEKSTI
sanonta = 'olipa kerran mies'
#isoilla ja pienillä kirjaimilla
print(sanonta.upper())
print(sanonta.lower())
#iso vai pieni?
print(sanonta.lower().isupper())
#kaksi riviä samaan
print("spfnf", end="")
#ei välejä
print("dgsgs", sep="--") jos halutaan -- joka väliin
#formalisoitu string
x = f"jotain {ympärys} jotain" {} jokin muuttuja
#tietty määrä desimaaleja
f"result: {3.14122145 *9 **2:.3f}"
#tulostuskentän leveys
print(f"1.·»{value}«")
print(f"2.·»{value:10}«")
print(f"3.·»{value:>10}«")
print(f"4.·»{value:<10}«")
print(f"5.·»{value:^10}«")
print(f"6.·»{value:2}«")
#pituus?
print(len(sanonta))
#tietty kohta tekstissä
print(sanonta[3])
#missä tietty asia on (mistä alkaa)?
print(sanonta.index('kerran'))
#korvaus
print(sanonta.replace('mies', 'nainen'))
#lista tekstiksi
lista = ['a','b','c']
print(''.join(lista))
#erottele pätkiä
print(vaelluspaikat.split(','))
#NUMEROT
#plus-, miinus-, kerto-, jako
print(1+2-3*4/5)
#muuttujana
numero = -3.2
print(numero/2)
#osaksi tekstiä
print('olen '+ str(numero) +' vuotias')
#itseisarvo
print(abs(numero))
#potenssi
print(pow(3,2))
#kumppi suurempi tai pienempi?
print(max(3,2))
print(min(2,3))
#pyöristys
print(round(numero))
#matikka moduuli
from math import *
#pyöristää ylös tai alas
print(ceil(numero))
print(floor(numero))
#nneliöjuuri
print(sqrt(3))

#INPUT
name = input('enter name:')
#tässä kohtaa kysyisi nimeä
print('hello ' + name)

#LISTAT
kaverit = ['konsta', 'matias', 'aarni']
vaelluspaikat = ['ukk', 'repovesi', 'ylläspallas']
print(kaverit)
#tietty arvo listasta
print(kaverit[2])
#arvon vaihto listassa
kaverit[2] = 'mösi'
#uusi arvo listaan
vaelluspaikat.append('evo')
#uusi arvo  tiettyyn kohtaan
vaelluspaikat.insert(2,'helvetinjärvi')
print(vaelluspaikat)
#listojen yhdistäminen
kaverit.extend(vaelluspaikat)
#montako samaa arvoa listassa?
print(kaverit.count('aarni'))
#montako arvoa listassa?
print(len(vaelluspaikat))
#missä kohtaa listaa
print(kaverit.index('aarni'))
#poistaa viimeisen arvon
vaelluspaikat.pop()
print(vaelluspaikat)
#poistaa arvon tietyltä paikalta
vaelluspaikat.remove('helvetinjärvi')
print(vaelluspaikat)
#aakkosjärjestys
kaverit.sort()
print(kaverit)
#käänteinen aakkosjärjestys
kaverit.reverse()
print(kaverit)
#kopioi listan
x = vaelluspaikat.copy()
print(x)
#poistaa kaikki arvot listasta
kaverit.clear()
print(kaverit)

#TUPLES
#kuin lista, jota ei voi muokata
koordinaatit = (3.4,2.3)
print(koordinaatit[1])

#FUNKTIOT
#kutsunta parametrin kanssa
def  sano_morjesta(nimi, ikä):
    print('morjesta ' + nimi + ikä + ' vee!')

sano_morjesta('mikko', str(19))
#return
#palauttaa halutun tiedon funktiosta käyttäjälle
def calc(x):
    return x*x
    print('tätä ei näytetä, sillä ei ole return')
result = calc(3)
print(result)
def kuutio(x):
    x*x
print(kuutio(3))
# 'none' tarkoittaa, että mitään ei palauteta, sillä ei return

#IF
onko_mies = False
sota_hirmuisa = True

if onko_mies:
    print('mies ulos sinusta')

else:
     print('toitteko mulle tyttärii?')

#jompikumpi
if onko_mies or sota_hirmuisa:
    print('päihittään se Hans!')
#molemmat vaaditaan
if onko_mies and sota_hirmuisa:
    print('päihittään se Hans!')

else: print('silkkaa kengänpohjan kuraa!')
#lisää  ehtoja
if onko_mies and sota_hirmuisa:
    print('päihittään se Hans!')

elif not(onko_mies):
    print('mieli niinkuin metsä')

else: print('sytytä talos palaa!')
#vertailu ehdoissa
def max_num(nro1, nro2, nro3):
    if nro1 >= nro2 and nro2 >= nro3:
        return nro1
    elif nro1 <= nro2 and nro2 >=3:
        return nro2
    else: return nro3

print(max_num(2,3,1))

#DICTIONARIES
kuukausimuunnoksia = {
    'Tamm': 'Tammikuu',
    'Helm': 'Helmikuu',
    'Maal': 'Maaliskuu',
}
#päällekkäisyyksiä ei sallista
#tietyn käyttö
print(kuukausimuunnoksia['Helm'])
#etsintä, jossa palaute, jos ei sanakirjassa
print(kuukausimuunnoksia.get('Huht', 'ei vielä lisätty'))

#WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i += 1

print('luupattu...')

#FOR LOOP
#annettu arvo muuttuu joka iteraatiolla
for kirjain in 'aakkonen':
    print(kirjain)
#listassa:
paikat = ['hml', 'tre', 'hki']
for paikka in paikat:
    print(paikka)
#numerojärjestys
for index in range(3,11):
    print(index)
#arvojen määrä listassa jonona
for index in range(len(paikat)):
    print(index)
#johonkin asti
for index in range(5):
    if index == 0:
        print('ensimmäinen')
    else:
        print('jälkimmäinen')
#eksponentti for loopilla
def korotus(kantaluku, eksponentti):
    vastaus = 1
    for index in range(eksponentti):
        vastaus = vastaus * kantaluku
    return vastaus
#input käyttäjältä samaan syssyyn
kantaluku = int(input('syötä kantaluku: '))
eksponentti = int(input('syötä eksponentti: '))
print(korotus(kantaluku, eksponentti))

#2D LISTAT
numero_ruudukko = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(numero_ruudukko[2][0]) # 3. rivin 1. arvo

#NESTED LOOP
for row in numero_ruudukko:
    for col in row:
        print(col)

#TRY
try:
    10/0
    nro = int(input('syötä kokonaisluku: '))
    print(nro)
except ValueError:
    print('KOKONAISLUKU')
except ZeroDivisionError as err:
    print(err)

#FILES
#pystytään käyttämään ulkopuolella tehtyä materiaalia koodissa
#lue ja käytä (ja sulje)
pakotus = open('Pakotus.txt','r')
#Pystyykö lukea?
print(pakotus.readable())
#lue kaikki
print(pakotus.read())
#Lue rivi
print(pakotus.readline()) #lukee 1. rivin
print(pakotus.readline()) #lukee 2. rivin
print(pakotus.readlines()) #lukee kaikki rivit järjestyksessä
pakotus.close() #muista aina sulkea myös tiedosto
#for loopissa
for sana in pakotus.readlines():
    print(sana)
pakotus.close()
#Lisätään tiedoston perään
pakotus = open('Pakotus.txt','a') #append
pakotus.write('\n naurattaahan se!') #jokaisella koodin suorituksella lisää tämän uudestaan!
#\n : uusi rivi
pakotus.close()
#päällekirjoitus
pakotus = open('Pakotus.txt','w')
pakotus.write('eipä ollutkaan!')
pakotus.close()
#uusi tiedosto
pakotus = open('Pakotus1.txt','w')
pakotus.close()

#MODUULIT JA PIP
#paljon moduuleja
#https://docs.python.org/3/py-modindex.html
#Mikä PIP versio (Terminaalissa)
>>> pip --version
#asennaa moduuli
>>> pip install 'python-docx'

#LUOKAT
#Luokan teko tiedosto:
class oppilas(): #oppilas datatyyppi
    def __init__(self, nimi, pääaine, arvosana, suomalainen):
    #määritetään ominaisuudet oppilaalle
        self.nimi = nimi
        self.pääaine = pääaine
        self.arvosana = arvosana
        self.suomalainen = suomalainen

    def kunniakirja(self): # : objekti
        if self.arvosana >= 4:
            return True
        else:
            return False
#toisessa tiedostossa:
from Testejä import oppilas #tiedostosta luokka

oppilas1 = oppilas('Mösi','Konetekniikka',3.4, True)
oppilas2 = oppilas('Meeri','Elintarvike kemia',4.2, True)

print(oppilas1.nimi) #näytä tietty ominaisuus tietystä datatyypin jäsenestä
print(oppilas2.pääaine) #älä käytä nimissä isoja kirjaimia!

print(oppilas2.kunniakirja())

#INHERITANCE
#toinen luokka perii toisen ominaisuudet
class kiinalainen_kokki(kokki):
#periminen päällekirjoittaa ominaisuudet

#INTERPETER
cmd terminnali
#mikä python versio?
>>> python3
#IP tiedot
>>> ipconfig
#Virtuaalinen ympäristö
py -3 -m venv .venv
.venv\scripts\activate

#kaikkien moduulien versiot
pip freeze

#API
#kutsun rakenne
url = "https://jokeapi.p.rapidapi.com/categories"

querystring = {"format":"json"}

headers = {
    'API_lähde': "jokeapi.p.rapidapi.com",
    'api_key': "cf1a8525bcmsh91a922241dc612ap1f6c08jsn88b106c1b578"
    }

syöte = requests.request(url, headers=headers, params=querystring)