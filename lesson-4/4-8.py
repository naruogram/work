import math
n=int(input("入力して下さい >>"))
r=1
L=(2*n*r)*math.sin((1/n)*math.pi)
result=L/(2*r)
print(result)