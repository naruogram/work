import math
def FanShape(r,theta,mode):
    if mode==1:
        return 2*math.pi*r*theta/360
    elif mode==2:
        return math.pi*r**2*theta/360
r=int(input("Input r  >> "))
theta=int(input("Input theta >> "))
mode=int(input("Input mode (1 or 2) >> "))
print(FanShape(r,theta,mode))