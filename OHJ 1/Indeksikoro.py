# COMP.CS.100 moro maailma
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

opintotuki = float(input('Enter the amount of the study benefits: '))
korko = 1.0117
korkoineen = float(opintotuki * korko)

print('If the index raise is 1.17 percent, the study benefit,')
print('after a raise, would be ' + str(korkoineen) + ' euros')

toinen_korko = float(korkoineen * korko)
print('and if there was another index raise, the study')
print('benefits would be as much as ' + str(toinen_korko) + ' euros')
