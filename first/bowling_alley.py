N, K = map(int, input().split())
mass = []
for i in range(K):
    mass.append([int(j) for j in input().split()])
line = []
for i in range(N):
    line.append('I')
for i in range(K):
    for j in range(mass[i][0] - 1, mass[i][1]):
        line[j] = '.'
for i in line:
    print(i)
