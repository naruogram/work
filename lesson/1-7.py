import math
numbers=[1,3,9,1/3,1/9]
bottom=3
for i in numbers:
    print(math.log(i, bottom))
print("------------------")
second_numbers=[1/3,1/9,1/27,1,3,9,27]
second_bottom=1/3
for k in second_numbers:
    print(math.log(k, second_bottom))