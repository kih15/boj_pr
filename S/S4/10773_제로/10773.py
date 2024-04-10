import sys
sys.stdin = open('input.txt')

K = int(input())
stack = []
for _ in range(1, K+1):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

num = 0
while stack:
    num += stack.pop()

print(num)