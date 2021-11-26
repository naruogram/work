import math
dx=2
s=0
for i in range(1,8):
    for j in range(1,dx+1,1):
        s+=4/dx*4/dx*j
    print(f"{dx}個の長方形で計算したとき={s}")
    s=0
    dx*=2
print("--------------------------------------------")
dx=2
s=0
for i in range(1,8):
    for j in range(1,dx+1,1):
        s+=math.pi/dx*math.sin(math.pi/dx*j)
    print(f"{dx}個の長方形で計算したとき={s}")
    s=0
    dx*=2