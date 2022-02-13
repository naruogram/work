def recurrence(n):
    if n ==0:
        return 2
    else:
        return recurrence(n-1)*
n=5
for i in range(n+1):
    print(f'{i}: {recurrence(i)}')