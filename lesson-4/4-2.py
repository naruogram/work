def recurrence(n):
    if n ==1:
        return 1
    else:
        return 2*recurrence(n-1)+3 
    
for i in range(1,11):
    print(f"{i}の時: {recurrence(i)}")
