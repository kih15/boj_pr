import sys
sys.stdin = open('input.txt')

s = input()
n = int(input())
cnt = 0
for _ in range(n):
    r = input()
    d_r = r + r
    if s in d_r:
        cnt += 1

print(cnt)