import sys


def func(tmp):
    sum = int()
    for i in tmp.upper():
        sum += ord(i) - ord('A')
    return sum


line = []
for i in sys.stdin:
    line.append(i)

print(*sorted(line, key=lambda i: (func(i), i)))
