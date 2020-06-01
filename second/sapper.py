length, width, count_of_bombs = map(int, input().split())
x = []
y = []
field = [[0 for i in range(width)] for j in range(length)]
for i in range(count_of_bombs):
    x, y = map(int, input().split())
    field[x - 1][y - 1] = '*'
for i in range(length):
    for j in range(width):
        sum = int()
        if field[i][j] != '*':
            if i != 0 and j != 0 and field[i - 1][j - 1] == '*':
                sum += 1
            if i != 0 and field[i - 1][j] == '*':
                sum += 1
            if i != 0 and j != width - 1 and field[i - 1][j + 1] == '*':
                sum += 1
            if j != 0 and field[i][j - 1] == '*':
                sum += 1
            if j != width - 1 and field[i][j + 1] == '*':
                sum += 1
            if i != length - 1 and j != 0 and field[i + 1][j - 1] == '*':
                sum += 1
            if i != length - 1 and field[i + 1][j] == '*':
                sum += 1
            if i != length - 1 and j != width - 1 and field[i + 1][j + 1] == '*':
                sum += 1
            field[i][j] = sum
        print(field[i][j], end=' ')
    print()
