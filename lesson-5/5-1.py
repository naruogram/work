import math
a=84
b=98
k=1
data=1
datas=[]
datas2=[]
#素因数分解
for i in range(2,a):
    k+=1
    if a%k==0:
        datas.append(k)
        a=a/k
        k-=1
datas.append(math.floor(a))
a=84
#素因数分解
k=1
for j in range(2,b):
    k+=1
    if b%k==0:
        datas2.append(k)
        b=b/k
        k-=1
datas2.append(math.floor(b))
b=98
#素因数分解の結果を使って、最大公約数を計算
for q in datas:
    for w in datas2:
        if q==w and q!=0:
            data=data*q
            datas.remove(q)
            datas2.remove(w)
            datas.insert(0,0)
            datas2.insert(0,0)
            break
print(f"{a}と{b}の最大公約数は{data}")