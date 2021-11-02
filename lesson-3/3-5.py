year=int(input(">>"))
if year%4==0:
    if year%400==0:
        print("うるう年です")
    elif year%100==0:
        print("うるう年ではないです")
    else:
        print("うるう年です")
else:
    print("うるう年ではないです")