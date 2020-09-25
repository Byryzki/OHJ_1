"""
COMP.CS.100 suuruus
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
def is_the_list_in_order(list):
    """

    :param list:
    :return:
    """

    if len(list) == 1:
        return True
    elif list == sorted(list):
        return True
    elif list != sorted(list):
        return False

def main():
    x = [1, 1, 1, 1, 2, 3]
    is_the_list_in_order(x)


if __name__ == "__main__":
    main()