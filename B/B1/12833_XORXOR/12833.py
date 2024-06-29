import sys
sys.stdin = open('input.txt')

a, b, c = map(int, input().split())
if c % 2 != 0:
    a ^= b
print(a)