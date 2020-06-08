N = int(input())

block = []
check = True

for i in range(N):
    a = int(input())
    block.append(dict())
    for j in range(a):
        tmp1, tmp2 = input().split()
        block[i][tmp1] = int(tmp2)
    if any(value == 0 for value in block[i].values()):
        check = False

if check:
    print("ДА")
else:
    print("НЕТ")
