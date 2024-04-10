import sys
sys.stdin = open('input.txt')

def bt(s):
    if len(path) == m:
        print(*path)
        return
    for i in range(s, n+1):
        path.append(i)
        bt(i)
        path.pop()

path = []
n, m = map(int, input().split())
bt(1)