# COMP.CS.100 zipbong
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

k = int(input("How many numbers would you like to have? "))

def main():
    i = 1
    for i in range(1,k+1):
        if i % 3 == 0 and i % 7 != 0:
            print("zip")
        elif i % 7 == 0 and i % 3 != 0:
            print ("boing")
        elif i % 3 == 0 and i % 7 ==0:
            print('zip boing')
        else:
            print(i)

if __name__ == '__main__':
    main()
