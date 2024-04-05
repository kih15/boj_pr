import sys
sys.stdin = open('input.txt')

T = int(input())
arr = []
for tc in range(1, T+1):
    a, b = map(int, input().split())
    arr.append([a, b])

arr = sorted(arr, key=lambda x: x[1])

for i in arr:
    print(*i)