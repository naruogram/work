import math
a=2
for i in range(2,16): 
    a=2**i
    r=1
    L=(2*a*r)*math.sin((1/a)*math.pi)
    result=L/(2*r)
    print(f"正{2**i}角形の近似値は{result}")
