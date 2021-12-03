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
        if judge(n)%4==1:
            _judge=False
            for a in range(1,judge(n)):
                for b in range(1,judge(n)):
                    if a**2+b**2==judge(n) and _judge==False:
                        print(f'{judge(13)} ={a}^2+{b}^2')
                        _judge=True
                        break
            n=int(input("Input prime number "))
            judge(n)
        else:
            print('Not surplus 1 (When diveded by 4)')
            n=int(input("Input prime number "))
            judge(n)
        continue