import sys
sys.stdin = open('input.txt')

def bt():
    if len(path) == m:
        print(*path)
        return
    for i in range(1, n+1):
        path.append(i)
        bt()
        path.pop()

path = []
n, m = map(int, input().split())
bt()