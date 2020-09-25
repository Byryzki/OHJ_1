"""
COMP.CS.100 Yogi Bear
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
"""
Varsinainen sanoitus, parametreinä hahmon nimi ja montako kertaa luritetaan
"""

def repeat_name(name, i):
    for i in range(0, i):
        print(f"{name}, {name} Bear")


def verse(vers, name):
    i = 3
    print(vers)
    print(f"{name}, {name}")
    print(vers)
    repeat_name(name, i)
    print(vers)
    print(f"{name}, {name} Bear")
    print()

def main():
    i = 3
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
