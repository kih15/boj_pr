import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input().rstrip())
q = []
for _ in range(n):
    s = list(map(str, input().split()))
    if s[0] == 'push':
        q.append(s[1])
    if s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if s[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    if s[0] == 'size':
        print(len(q))
    if s[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    if s[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)

