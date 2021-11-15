import math

a=int(input("a >>"))
b=int(input("b >>"))
c=int(input("c >>"))
d=(b**2-4*a*c)
if a!=0:
  if d>0:
    x_1=(-b+math.sqrt(d))/(2*a)
    x_2=(-b-math.sqrt(d))/(2*a)
    print(f"答えは: {x_1},{x_2}")
  elif d==0:
    x_1=-b/(2*a)
    print(f"答えは: {x_1}")
  else:
    x_1=(-b+math.sqrt(-d)*1j)/(2*a)
    x_2=(-b-math.sqrt(-d)*1j)/(2*a)
    print(f"答えは: {x_1},{x_2}")
else:
    x_1=(-c/b)
    print(f"答えは: {x_1}")