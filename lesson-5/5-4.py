LIMIT = 10**-20
 
def f(x):
    return x*x - 2

xn1 = 2
xn0 = 1


while (xn1 - xn0) * (xn1 - xn0) > LIMIT:
    xm = (xn1 + xn0) / 2
    if f(xm) > 0:
        xn1 = xm
    else:
        xn0 = xm
print(f"近似値は{(xn1+xn0)/2}")