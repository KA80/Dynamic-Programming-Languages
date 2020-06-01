N = int(input())
a = [int(i) for i in input().split()]
K = int(input())
a = a[-K % N:] + a[:-K % N]
print(' '.join([str(i) for i in a]))
