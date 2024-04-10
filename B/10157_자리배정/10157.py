import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())
K = int(input())
arr = [[0] * C for _ in range(R)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

direct = 0
i = 0
j = 0
num = 1
arr[i][j] = num
num += 1
if C * R < K:
    print(0)
else:
    while num <= K:
        ni = i + di[direct]
        nj = j + dj[direct]
        if 0 <= ni <= C and 0 <= nj <= R and arr[ni][nj] == 0:

            i = ni
            j = nj
            arr[i][j] = num
            num += 1

        else:
            direct = (direct+1) % 4

print(arr)

print(i+2, j-2)