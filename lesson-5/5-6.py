n=int(input("Input prime number "))
jugde=0
for i in range(n,2,-1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        jugde=i
        break
while n==n:
    if n==jugde:
        a=int(input("Input integer number "))
        print(f"Division: {a**n}\nSurplus: {a**n%n}")
    elif n==0 or n<0:
        print("Not prime number")
        break
    else:
        n=int(input("Input prime number "))
        continue
