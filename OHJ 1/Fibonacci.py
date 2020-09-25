# COMP.CS.100 fibonacci
# Tekijä: Pyry Laine
# Opiskelijanumeroni: 050282836

f=[1,1,2]
ff=[f[0]+f[1], ]
fib = range(1, 10, )

def main():
    i = 1
    e = 1
    t = 1
    k = int(input("How many Fibonacci numbers do you want? "))
    while i <= k:
        if i == 1:
            print("1. 1")
            i +=1
        elif i == 2:
            print("2. 1")
            i +=1
        else:
            sum = e+t
            print(i, ". " , sum , sep='')
            e=t
            t=sum
            i +=1

if __name__ == "__main__":
    main()
