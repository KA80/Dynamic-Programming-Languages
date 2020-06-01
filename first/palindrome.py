line = ''.join(input().split())
palindrome = 1
for i in range(int(len(line) / 2)):
    if line[i] != line[-i - 1]:
        palindrome = 0
if palindrome == 1:
    print("YES")
else:
    print("NO")
