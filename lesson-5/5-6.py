n=int(input("Input prime number "))
judge=0
def prime(n):
    if n!=2 or n!=0:
        for i in range(n,2,-1):
            for j in range(2, i):
                if i % j == 0:
                    print("Not prime number")
                    n=int(input("Input prime number "))
                    continue
            else:
                judge=i
                return judge
    else:
        if n==0:
            print("END")
            return 0
        else:
            judge=2
            return judge

while True:
    if n==prime(n):
        a=int(input("Input integer number "))
        print(f"Division: {a**n}\nSurplus: {a**n%n}")
        n=int(input("Input prime number "))
        prime(n)
        continue
    elif n==0 or n<0:
        print("End")
        break
    else:
        n=int(input("Input prime number "))
        continue
