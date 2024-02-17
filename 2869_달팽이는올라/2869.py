import sys
sys.stdin = open('input.txt')

A, B, V = map(int, input().split())
v = 0 # 움직인 거리
i = 0 # 일 수
while True:
    i += 1
    if A*i - B*(i-1) >= V:
        break
print(i)