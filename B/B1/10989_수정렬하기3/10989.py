import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
tmp = [0]*10001
N = int(input())
for i in range(N):
    n = int(input())
    tmp[n] += 1

for i in range(10001):
    if tmp[i] > 0:
        for _ in range(tmp[i]):
            print(i)
