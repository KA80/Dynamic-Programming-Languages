N = int(input())
mass = [int(i) for i in input().split()]
height = int(input())
num = 1
for i in range(N):
    if height <= mass[i]:
        num += 1
print(num)

