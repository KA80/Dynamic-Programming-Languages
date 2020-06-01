N = int(input())

parents = {}
bloodline = {}
for i in range(N - 1):
    child, parent = input().split()
    parents[child] = 0
    parents[parent] = 0
    bloodline[child] = parent
    if parent not in bloodline:
        bloodline[parent] = 0

for i in sorted(bloodline):
    counter = 0
    way = i
    while bloodline[way]:
        way = bloodline[way]
        counter += 1
    parents[i] = counter

for i in sorted(parents):
    print(i, int(parents[i]))
