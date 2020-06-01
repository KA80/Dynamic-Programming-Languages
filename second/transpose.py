n, m = map(int, input().split())
matrix = [[int(i) for i in input().split()] for i in range(n)]
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
