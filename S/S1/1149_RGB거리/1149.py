import sys
sys.stdin = open('input.txt')

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]

for j in range(3):
    dp[0][j] = rgb[0][j]

for i in range(1, n):
    dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])

min_cost = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(min_cost)
