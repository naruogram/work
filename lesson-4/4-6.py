data=0
for i in range(1,11):
    for k in range(1,i*2):
        if k%2!=0 and k<=i*2:
           data+=k
    print(f"{i}の2乗は{i**2}")
    print(f"{i}までの奇数の和は{data}")
    data=0