import sys
sys.stdin = open('input.txt')

num = input()
n = len(num)
a = 0
b = 0
for i in range(n):
    if i < n / 2:
        a += int(num[i])
    else:
        b += int(num[i])

if a == b:
    print('LUCKY')
else:
    print('READY')