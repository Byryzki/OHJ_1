# COMP.CS.100 teksti
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

if __name__ == "__main__":
    main()
