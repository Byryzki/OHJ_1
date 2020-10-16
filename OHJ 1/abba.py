"""
COMP.CS.100 Nimikääntäjä
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def main():
    sana = "abbabbabba"
    count_abbas(sana)

def count_abbas(sana):
    """

    :param sana: testisana
    :return: abba: lkm.
    """
    k=0
    if len(sana) < 4:
        return 0
    else:
        for i in range(0, len(sana)):
            if sana[i: i+4] == "abba":
                k +=1
            else:
                pass
        return k

if __name__ == "__main__":
    main()