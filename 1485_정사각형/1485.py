import sys
sys.stdin = open('input.txt')

T = int(input())
point = []
for i in range(T*4):
    x, y = map(int, input().split())
    print(x, y)
    s = (x, y)
    point.append(s)
print(point)