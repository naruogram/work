import math
numbers=[1,3,9,1/3,1/9]
bottom=3
# 底が3で，1, 3, 9, 1/3, 1/9の対数の値
for i in numbers:
    print(math.log(i, bottom))
print("------------------")
# 底が1/3で，1/3, 1/9, 1/27, 1, 3, 9, 27の対数の値
second_numbers=[1/3,1/9,1/27,1,3,9,27]
second_bottom=1/3
for k in second_numbers:
    print(math.log(k, second_bottom))