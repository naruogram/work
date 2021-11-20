N=int(input("Input loan >>"))
a=int(input("Input rate >>"))/100+1
b=int(input("Input return amount >>"))
count=0
while N>0:
    if N*a-N<b:
        N=N*a-b
        count+=1
        continue
    else:
        print("You can't return money")
        break
if count!=0:
    print(f"Finished in {count} years")