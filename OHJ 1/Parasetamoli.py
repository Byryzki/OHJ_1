"""
COMP.CS.100 Parasetamoli
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""

def calculate_dose(paino, aika, annos):
    """laskee ja palaauttaa oikean annoksen, kun annetaan paino, aika edellisestä annoksesta
    , aiempi vuorokauiannos jos OD niin palauttaa 0"""
    sk = int(15*paino)
    koko = int(sk + annos)
    anto = sk

    if annos == 0:
        anto = sk
    elif aika < 6:
        anto = 0
    elif koko > 4000:
        anto = 4000 - annos

    return anto

def main():
    """päätoiminto"""
    paino = int(input("Patient's weight (kg): "))
    aika = int(input("How much time has passed from the previous dose (full hours): "))
    annos = int(input("The total dose for the last 24 hours (mg): "))

    calculate_dose(paino, aika, annos)
    print("The amount of Parasetamol to give to the patient:", calculate_dose(paino, aika, annos))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()