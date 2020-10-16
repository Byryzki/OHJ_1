"""
COMP.CS.100 aakkosjärjestys (pisin)
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def main():
    sana = "acegabcdefga" #pitäisi tulla abcdee
    longest_substring_in_order(sana)

def longest_substring_in_order(sana):
    """
    
    :param sana: syötetty sana
    :return: pisin aakkosjärjestys
    """
    pienin = ""
    keski = ""
    suurin = ""
    for i in sana:
        if pienin < i:
            suurin += i
            if len(suurin) > len(keski):
                keski = suurin
        else:
            suurin = i
        pienin = i

    return keski

if __name__ == "__main__":
    main()