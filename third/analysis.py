import sys

data = {}
for i in sys.stdin:
    word = i.split()
    for j in range(len(word)):
        data[word[j]] = data.get(word[j], 0) + 1

sorted_data = sorted(data.items(), key=lambda i: (-int(i[1]), i[0]))

for i in range(len(sorted_data)):
    print(sorted_data[i][0])
