import math
numbers_division=[]
numbers_add=[]
n=int(input(">> "))
for i in range(1,n+1):
    numbers_division.append(math.floor(n%2))
    n=math.floor(n/2)
for i in range(0,8):
    numbers_add.append(numbers_division[i])
numbers_add.reverse()
result = "".join([str(_) for _ in numbers_add])
print(result)
