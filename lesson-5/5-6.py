n=int(input("Input prime number "))
judge=0
def prime(n):
    if n%2!=0 and n!=0:
        for i in range(n,2,-1):
            for j in range(2, i):
                if i % j == 0:         
                    print("Not prime number")
                    return n      
                else:
                    judge=i
                    return judge
    else:
        if n==0:
            print("END")
            return 0
        elif n==2:
            judge=2
            return judge
        else:
            print("Not prime number")
            return n

while True:
    if n==prime(n):
        a=int(input("Input integer number "))
        print(f"Division: {a**n//n}\nSurplus: {a**n%n}")
        n=int(input("Input prime number "))
        continue
    elif prime(n)==0 or prime(n)<0:
        print("End")
        break
    else:
        n=int(input("Input prime number "))
        continue
