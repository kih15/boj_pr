import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = 1
for i in range(N):
    cnt += 6*i
    if N <= cnt:
        print(1+i)
        break

# 1, 2~7, 8~19, 20~37, 38~61, ...
#   6, 12, 18, 24
