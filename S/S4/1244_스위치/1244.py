import sys
sys.stdin = open('input.txt')

s = int(input()) # 스위치 개수
arr = list(map(int, input().split())) # 스위치 상태
std = int(input())  # 학생 수
for _ in range(std):
    g, n = map(int, input().split())
# arr = [0, 1, 0, 1, 0, 0, 0, 1]
    if g == 1:
        for i in range(s):
            if (i+1) % n == 0: # 인덱스 0~7이니까
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
    else:
        n -= 1  # 여학생이 받은 수와 left right 변수의 인덱스를 맞추기 위해서
        left = right = n
        while left >= 0 and right < s:
            if arr[left] == arr[right]:
                if arr[left]:
                    arr[left] = 0
                    arr[right] = 0
                else:
                    arr[left] = 1
                    arr[right] = 1
            else:
                break
            left -= 1
            right += 1

for i in range(0, s, 20):
    print(*arr[i:i+20])
