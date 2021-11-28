LIMIT = 10**-20
 
def f(x):
    return x*x - 2

xn1 = float(input("xn1を入力してください"))
while f(xn1)<0:
    xn1 = float(input("xn1を入力してください"))
    continue
xn0 = float(input("xn0を入力してください"))
while f(xn0)>0:
    xn0 = float(input("xn0を入力してください"))
    continue

while (xn1 - xn0) * (xn1 - xn0) > LIMIT:
    xm = (xn1 + xn0) / 2
    if f(xm) > 0:
        xn1 = xm
    else:
        xn0 = xm
    print(f"近似値は{(xn1+xn0)/2}")