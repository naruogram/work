def MyReversed(n):
    array=[]
    for i in  reversed([int(a) for a in str(n)]):
        if i!=0:
            array.append(i) 
    result = int("".join([str(_) for _ in array]))
    return result
n=int(input(">>"))
print(MyReversed(n))