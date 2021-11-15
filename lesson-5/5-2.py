num=int(input("Input natural number >>"))

while num==num:
    if num==0:
        print("End")
        break
    elif num<0:
        num=int(input("Input natural number >>"))
        continue
    print(num**2)
    num=int(input("Input natural number >>"))
    continue