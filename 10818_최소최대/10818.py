import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
min_v = arr[0]
max_v = arr[0]
for i in arr:
    if min_v > i:
        min_v = i
    if max_v < i:
        max_v = i
print(min_v, max_v)
