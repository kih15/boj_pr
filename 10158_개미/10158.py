import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 0 1 2 3 4 5 6 (5 4 3 2 1)   w 안에서 움직임
# 0 1 2 3 4 5 6 (7 8 9 10 11) t+p

dx = (t+p) % (2*w)
dy = (t+q) % (2*h)

if dx > w:  # w 에 부딪히면 감소해야하니까
    dx = 2*w - dx
if dy > h:
    dy = 2*h - dy
print(dx, dy)