"""
COMP.CS.100 montako löytyy
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def are_all_members_same(list):
    """

    :param list:
    :return:
    """
    try:
        if len(list) == 1:
            return True
        elif min(list) == max(list):
            return True
        elif min(list) != max(list):
            return False
    except:
        return True
def main():
    x = [1,1,1,1,1,1,1]
    are_all_members_same(x)

if __name__ == "__main__":
    main()