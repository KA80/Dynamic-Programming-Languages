
nums = [int(i) for i in range(10, 100)]
nums = filter(lambda x: x % 9 == 0, nums)

print(sum(map(lambda i: i ** 2, nums)))