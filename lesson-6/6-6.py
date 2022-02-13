def MyReversed(n):
    array=[]
    while True:
        if n>0:
            for i in reversed([int(a) for a in str(n)]):
                array.append(i)
            result = int("".join([str(_) for _ in array]))
            return result           
        elif n<1:
            print("Input number again")
            n=int(input(">>"))
            continue
n=int(input(">>"))
print(MyReversed(n))