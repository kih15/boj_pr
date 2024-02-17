import sys
sys.stdin = open('input.txt')

N = int(input())
M = 1000

arr = [[0] * (M + 1) for _ in range(M + 1)]

for k in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            arr[i][j] = k   # 중복되는 부분은 마지막에 붙인 종이로 할당

for k in range(1, N+1):
    cnt = 0
    for i in range(M+1):
        for j in range(M+1):
            if arr[i][j] == k: # 겹치는 부분은 마지막 종이 값을 가지니까 cnt에 증가가 안된다.
                cnt += 1
    print(cnt)

