N = int(input())

vocabulary = {}
counter = 0
for i in range(N):
    eng, lat = input().split(" - ")
    lat = lat.split(", ")
    for j in lat:
        if j not in vocabulary:
            counter += 1
            vocabulary[j] = []
        vocabulary[j].append(eng)

print(counter)
for i in sorted(vocabulary):
    tmp = ', '.join(sorted(vocabulary[i]))
    print(i + ' - ' + tmp)