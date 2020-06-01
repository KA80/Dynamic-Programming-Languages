N = int(input())

file = {}

for i in range(N):
    name, *available_actions = input().split()
    file[name] = available_actions
    del name

M = int(input())

possible_actions = {'write': 'W', 'read': 'R', 'execute': 'X'}

for i in range(M):
    action, name = input().split()
    action_code = possible_actions[action]
    if action_code in file.get(name):
        print("OK")
    else:
        print("Access denied")
