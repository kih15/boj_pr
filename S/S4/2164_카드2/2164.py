from collections import deque
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
d = deque()
for i in range(1, n+1):
    d.append(i)
while True:
    if len(d) == 1:
        print(*d)
        break
    d.popleft()
    d.append(d.popleft())