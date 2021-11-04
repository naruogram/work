for i in range(0,10):
    for k in range(1,10):
        #上の方に何の段を表示する
        if i==0:
            #kが１である時最初に空白を入れる
            if k==1:
                print(end="    ")
            #数字を入れていく
            print(k,end="  ")
        #最初に何の段を表示する
        if k==1 and i>0:
            print(f"{i}: ",end=" ")
            #次の数字が1桁の場合の処理
            if i>0 and i*(k+1)<10:
                print(i*k,end="  ")
            else:
                print(i*k,end=" ")
        #kが２以降の処理(整える処理)
        if k==2 and i>0:
            if i*(k+1)<10 and i>0:
               print(i*k,end="  ")
            else:
               print(i*k,end=" ")
        #kが3以上の時の処理
        if k>=3 and i>0:
            if i*(k+1)<10 and i>0:
               print(i*k,end="  ")
            else:
               print(i*k,end=" ")
    #改行
    print("")