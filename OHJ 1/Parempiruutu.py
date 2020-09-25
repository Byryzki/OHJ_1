"""
COMP.CS.100 Kulmat
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
# TODO: the definition of print_box goes here unless it goes after main.
def print_box(width, height, border_mark="#",inner_mark=" "):
    """

    :param width:
    :param height:
    :param border_mark:
    :param inner_mark:
    :return:
    """
    print(border_mark*width)
    for i in range(0, height-2):
        print(border_mark, inner_mark*(width-2), border_mark, sep="")
    print(border_mark * width)
    print()

def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
