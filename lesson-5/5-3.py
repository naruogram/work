import math
N=int(input("Input loan >>"))
a=float(input("Input rate >>"))/100+1
b=int(input("Input return amount >>"))
count=1
amount=N
while N>0:
    if N*a-N<b:
        N=math.floor(N*a)
        print(f"Year {count}:{N}")
        N=N-b
        count+=1
        continue
    else:
        print("You can't return money")
        break
if count!=1:
    print(f"Finished in {count} years")
