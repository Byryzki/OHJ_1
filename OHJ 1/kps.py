# COMP.CS.100 moro maailma
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

p1 = str(input('Player 1, enter your choice (R/P/S): '))
p2 = str(input('Player 2, enter your choice (R/P/S): '))

R = 'R'
P = 'P'
S = 'S'

def main():
    if p1 == R and p2 == P:
        print('Player 2 won!')
    elif p1 == R and p2 == S:
        print('Player 1 won!')
    elif p1 == P and p2 == S:
        print('Player 2 won!')
    elif p1 == P and p2 == R:
        print('Player 1 won!')
    elif p1 == S and p2 == R:
        print('Player 2 won!')
    elif p1 == S and p2 == P:
        print('Player 1 won!')
    elif p1 == p2:
        print("It's a tie!")
    else:
        print('ropleema!')

main()