import sys
sys.stdin = open('input.txt')


t = int(input())
for _ in range(t):
    n = int(input())

    max_L = 0
    max_s = ''
    for _ in range(n):
        s, l = input().split()
        L = int(l)

        if L > max_L:
            max_L = L
            max_s = s
    print(max_s)