import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
cnt = 0
for i in range(n+1):
    for j in range(m+1):
        cnt += 1
print(cnt)
