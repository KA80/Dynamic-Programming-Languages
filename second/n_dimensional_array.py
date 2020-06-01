
def array(x):
    if x <= 1:
        return [0, 0]
    return [array(x - 1)] + [array(x - 1)]


n = int(input())
print(array(n))
