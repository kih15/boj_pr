import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    S = input()
    cnt = 0
    res = 0
    for i in range(len(S)):
        if S[i] == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)