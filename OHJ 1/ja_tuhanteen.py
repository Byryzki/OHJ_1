# COMP.CS.100 Vaihtorahat
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

hinta = int(input('Purchase price: '))
maksu = int(input('Paid amount of money: '))

kympit = ((maksu - hinta) // 10)
kympitt = ((maksu - hinta)%10)

vitoset = (kympitt//5)
vitosett = (kympitt%5)

kakkoset = (vitosett // 2)
kakkosett = (vitosett % 2)

ykkoset = (kakkosett // 1)

def main():
    if hinta >= maksu:
        print('No change')
    else:
        print('Offer change:')
        if kympit > 0:
            print(int(kympit) , 'ten-euro notes')
        if vitoset > 0:
            print(int(vitoset) , 'five-euro notes')
        if kakkoset > 0:
            print(int(kakkoset) , 'two-euro coins')
        if ykkoset > 0:
            print(int(ykkoset) , 'one-euro coins')

main()