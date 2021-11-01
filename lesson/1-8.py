import math
P=40/100
Q=90/100
result=-P*math.log(P,2)
result2=-Q*math.log(Q,2)
print(result)
print(result2)
print(result>result2)
# 上記のことから情報量の大きさが低下していることがわかる