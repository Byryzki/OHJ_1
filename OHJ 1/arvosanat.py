"""
COMP.CS.100 suuruus
Tekijä: Pyry Laine
Opiskelijanumeroni: 050282836
"""
# TODO: add the definition for convert_grades here
def convert_grades(x):
    """

    :param x: hjkjhgfdwertyu
    :return:
    """
    for i in range(0, len(x)):
        if x[i] >= 1 and x[i] <= 5:
            x[i] = 6
        elif x[i] == 0:
            x[i] = 0

def main():
    grades = []
    convert_grades(grades)
    print(convert_grades(grades))  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
