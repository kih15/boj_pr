import sys
sys.stdin = open('input.txt')

n = int(input())
a = 0
b = 1
for _ in range(n):
    b += a
    a = b - a
print(a)