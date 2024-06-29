from collections import deque
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
d = deque()
for _ in range(n):
    s = list(map(str, input().split()))
    if s[0] == 'push_front':
        d.appendleft(s[1])
    if s[0] == 'push_back':
        d.append(s[1])
    if s[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    if s[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    if s[0] == 'size':
        print(len(d))
    if s[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    if s[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    if s[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)