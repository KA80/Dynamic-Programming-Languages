n = int(input())
fibonacci = []
for i in range(n):
    if 0 <= i <= 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
for i in fibonacci:
    print(i, end=' ')
