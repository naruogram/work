a=170.3
b=164.7
c=183.9
d=159.2
e=175.8
m=(a+b+c+d+e)/5
data=[a,b,c,d,e]
datas=0
result=0
# dataの配列を回して、それぞれ計算する
for i in data:
    datas=(i-m)**2
    result+=datas
v=result/5
print(v)