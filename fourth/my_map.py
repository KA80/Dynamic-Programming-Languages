def my_map(operation, values):
    return [operation(i) for i in values]


values = [int(i) for i in input().split()]
operation = lambda x: x + 5
print(*my_map(operation, values))