import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
bag = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        bag[x] = k
print(*bag[1:])