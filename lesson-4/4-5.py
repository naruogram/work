even_numbers=[]
data=1
#偶数を見つける
for i in range(1,11):
    if i%2==0:
        even_numbers.append(i)
#累乗の計算
for k in range(0,len(even_numbers)):
    for j in range(1,even_numbers[k]):
        data+=data*j
    print(f"Factoria({even_numbers[k]}):{data}")
    data=1