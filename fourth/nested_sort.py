def my_sorted(data, key=lambda x: -x):
    sorted_data = []
    for element in data:
        sorted_data.append(sorted(element, key=key))
    return sorted(sorted_data, key=lambda i: i[-1])


data = [[6, 5, 4], [3, 6], [1]]
key = lambda x: x
print(my_sorted(data, key=key))
