import sys
sys.stdin = open('input.txt')

l, p = map(int, input().split())
arr = list(map(int, input().split()))
tmp = []
for i in range(len(arr)):
    tmp.append(arr[i] - l*p)
print(*tmp)