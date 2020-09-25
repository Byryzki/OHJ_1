# COMP.CS.100 moro maailma
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

tunne = int(input('How do you feel? (1-10) '))

def main():
    if tunne > 7 and tunne < 10:
        print('A suitable smiley would be :-)')
    elif tunne == 10:
        print('A suitable smiley would be :-D')
    elif tunne <= 7 and tunne >= 4:
        print('A suitable smiley would be :-|')
    elif tunne < 4 and tunne > 1:
        print('A suitable smiley would be :-(')
    elif tunne == 1:
        print("A suitable smiley would be :'(")
    else:
        print('Bad input!')

main()