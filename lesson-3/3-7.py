c1=input("Input one alphabet character 1>")
c2=input("Input one alphabet character 2>")
big_c1=chr(ord(c1)-32)
big_c2=chr(ord(c2)-32)
small_c1=chr(ord(c1)+32)
small_c2=chr(ord(c2)+32)
if len(c1)==1:
    if 65<=ord(c1)<=90:
        print(small_c1)
    elif 97<=ord(c1)<=122:
        print(big_c1)
    else:
        print("アルファベットを入力してください")
if len(c2)==1:
    if 65<=ord(c2)<=90:
        print(small_c2)
    elif 97<=ord(c2)<=122:
        print(big_c2)       
    else:
        print("アルファベットを入力してください")

    