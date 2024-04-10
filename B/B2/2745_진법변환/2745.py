import sys
sys.stdin = open('input.txt')

n, b = map(str, sys.stdin.readline().split())
b = int(b)
print(int(n, b))