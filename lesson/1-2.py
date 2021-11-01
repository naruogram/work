import math
prime_number=[]
set_number=71
# 素数判定
for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_number.append(i)
# 71を10以下の素数で割る
for k in prime_number:
    print(f"71を{k}でわりました")
    print(math.floor(set_number/k))
    print(set_number%k)