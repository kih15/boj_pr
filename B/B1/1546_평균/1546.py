import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
max_v = arr[0]
for i in range(N):
    if max_v < arr[i]:
        max_v = arr[i]
avg = 0
for i in range(N):
    avg += arr[i] / max_v * 100 / N
print(avg)
