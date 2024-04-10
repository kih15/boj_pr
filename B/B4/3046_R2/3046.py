import sys
sys.stdin = open('input.txt')

r1, s = map(int, input().split())
# s = (r1 + r2) // 2
# 2*s = r1 + r2
r2 = 2*s - r1
print(r2)