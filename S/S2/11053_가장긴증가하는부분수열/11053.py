import sys
sys.stdin = open('input.txt')

n = int(input())
a = list(map(int, input().split()))
c = 1
for i in range(1, n):
    if a[i] < a[i-1]:
        continue
    else:
        c += 1
print(c)