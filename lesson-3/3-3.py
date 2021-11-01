score=int(input(">>"))
if score>100 or score<0:
    print("Values should be 0 and more, or less than 101.")
elif score>=90:
    print("S")
elif 90>score>=80:
    print("A")
elif 80>score>=70:
    print("B")
elif 70>score>=60:  
    print("C")
else:
    print("F")