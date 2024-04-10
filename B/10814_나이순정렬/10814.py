import sys
sys.stdin = open('input.txt')

arr = []
T = int(input())
for tc in range(1, T+1):
    a, n = map(str, input().split())
    arr.append([int(a), n])

arr = sorted(arr, key=lambda x: x[0])

for i in arr:
    print(*i)