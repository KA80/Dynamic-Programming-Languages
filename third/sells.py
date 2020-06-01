import sys

database = {}
for i in sys.stdin:
    man, *info_good = i.split()
    if man not in database:
        database[man] = dict()
    if info_good[0] in database[man]:
        database[man][info_good[0]] += int(info_good[1])
    else:
        database[man][info_good[0]] = int(info_good[1])

for i in sorted(database):
    print(i + ":")
    for j in sorted(database[i]):
        print(str(j) + " " + str(database[i][j]))
