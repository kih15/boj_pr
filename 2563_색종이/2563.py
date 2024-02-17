import sys
sys.stdin = open('input.txt')

N = int(input())
M = 100 # 가로세로의 크기가 100인 도화지
arr = [[0]*M for _ in range(M)] # 가로세로의 크기가 100인 빈 도화지
count = 0
for _ in range(N):
    # a 는 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
    # b는 아래쪽 변과 도화지 아래쪽 변 사이의 거리
    a, b = map(int, input().split())
# arr에 색종이의 넓이만큼 인덱스에 +1씩 해준다
# 그리고 != 0 인 부분을 다 더해주자
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] += 1
            # 반복문 돌면서 arr[i][j]가 1인 경우에 count가 1씩 증가하고
            # 반복문 안에 있으니까 arr[i][j]가 2부터는 count가 안되는 듯?
            if arr[i][j] == 1:
                count += 1
# print(arr)
# for row in arr:
#     print(' '.join(map(str, row)))
print(count)