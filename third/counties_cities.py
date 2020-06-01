N = int(input())

cities = {}
for i in range(N):
    country, *cities_tmp = input().split()
    for j in cities_tmp:
        cities[j] = country

M = int(input())

for i in range(M):
    city = input()
    print(cities[city])