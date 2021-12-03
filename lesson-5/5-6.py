n=int(input("Input prime number "))
#判定
def judge(n):
    prime=[]
    if n==2:
        prime.append(n)
    elif n==0:
        return 0
    elif n<2:
        return 1
    for i in range(n,2,-1):
        for k in range(2,i):
            if i%k==0:
                break
            else:
                prime.append(i)
                break
    if n==prime[0]:
        return prime[0]
    else:
        return 1

while True:
    if judge(n)==0:
        print("End")
        break
    elif judge(n)==1:
        print("Not prime number")
        n=int(input("Input prime number "))
        judge(n)
    else:
        a=int(input("Input integer number "))
        print(f"Division: {a**judge(n)//judge(n)}\nSurplus: {a**judge(n)%judge(n)}")
        n=int(input("Input prime number "))
        judge(n)
        continue