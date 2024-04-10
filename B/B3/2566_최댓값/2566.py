import sys
sys.stdin = open('input.txt')

n = 9
arr = [list(map(int, input().split())) for _ in range(n)]
max_v = 0
for i in range(n):
    for j in range(n):
        if max_v < arr[i][j]:
            max_v = arr[i][j]

print(max_v)
for i in range(n):
    for j in range(n):
        if arr[i][j] == max_v:
            print(i+1, j+1)
