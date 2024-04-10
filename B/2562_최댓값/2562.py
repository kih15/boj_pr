import sys
sys.stdin = open('input.txt')

max_v = 0
arr = []
for i in range(9):
    N = int(input())
    arr.append(N)
    if max_v < N:
        max_v = N
    if max_v == arr[i]:
        res = i+1
print(max_v)
print(res)