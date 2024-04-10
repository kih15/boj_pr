import sys
sys.stdin = open('input.txt')

n = 4
N = 100
area = [[0] * (N+1) for _ in range(N + 1)]
cnt = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            if area[i][j] == 0:
                area[i][j] += 1
                cnt += 1
print(cnt)

