import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())

    data = str(a ** b)
    print(data[-1])