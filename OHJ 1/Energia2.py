
def lista():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    # Testiarvo käyttäjän syötteille, jotta niitä ei tarvitse
    # aina naputella näppäimistöltä, kun haluat testata ohjelmaasi.
    # Tämä täytyy kuitenkin poistaa ja syötteet lukea oikeasti
    # käyttäjältä ennen Plussaan palauttamista. Muuten testit
    # eivät mene läpi.
    lista = []

    on = True
    while on == True:
        input_data = input("Enter energy consumption (kWh):")
        if input_data == "":
            break
        elif int(input_data) < 0:
            print(f"You entered: {input_data}. Enter non-negative numbers only!")
        else:
            lista.append(input_data)

    lista = sorted(lista)

    return lista

def luokat(lista):
    if lista ==[]:
        luokkia = 0
    else:
        maks = max(lista)
        luokkia = len(maks)

    return luokkia

def luokatlistaan(luokkia):
    luokkalista = [0] * luokkia
    return luokkalista

def tuloste(lista, luokkalista):
    if luokkalista == []:
        print("Nothing to print. Done.")
    else:
        for i in lista:
            ind = len(str(i))-1
            luokkalista[ind] +=1

        valit = len(luokkalista) * 2 - 2

        for vali in range(valit):
            print("", end="")

        valit = valit -2

        print("0-9: ", end="")
        for luokka in range(luokkalista[0]):
            print("*", end="")
        print()

        eka = 10
        vika = (eka*10)-1

        for i in range(1, len(luokkalista)):
            for vali in range(valit):
                print("", end="")
            valit = valit -2
            print(f"{eka}-{vika}:", end="")
            for a in range(luokkalista[i]):
                print("*", end="")
            print()
            eka = eka*10
            vika = eka*10 -1

def main():
        list = lista()
        jotain = luokat(list)
        luokkalista = luokatlistaan(jotain)
        tulosta = tuloste(list, luokkalista)

if __name__ == "__main__":
    main()
