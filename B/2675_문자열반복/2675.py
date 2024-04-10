import sys
sys.stdin = open('input.txt')

T = int(input())
P = ''
for tc in range(1, T+1):
    R, S = input().split()
    R = int(R)
    S = list(S)

    for i in range(len(S)):
        print(S[i] * R, end = '')
    print()