x=int(input(">>"))
y=int(input(">>"))
if x<y and (x%2==0 or y%2==0):
    print(f"{x} は {y} より小さく，かつ，{x} と {y} のどちらかが偶数である")

if (x<=10 or x>=100) and 100>=y>=10:
    print(f"{x} は 10 以下または 100 以上で，かつ，{y} は 10 以上かつ 100 以下である")