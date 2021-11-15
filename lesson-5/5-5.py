prime_number=[]
for i in range(2, 21):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")

for i in range(10000, 1,-1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print("")
        print(f"最も10000に近い素数は{i}")
        break