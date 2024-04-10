import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n, k = map(int, input().split())
coin = []
cnt = 0
for i in range(n):
    a = int(input())
    coin.append(a)
coin.reverse()

for i in coin:
    cnt += k//i
    k %= i
print(cnt)

