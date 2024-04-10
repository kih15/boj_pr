import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    arrA = list(map(int, input().split()))[1:]
    arrB = list(map(int, input().split()))[1:]
    tempA = [0] * 5
    tempB = [0] * 5
    for i in arrA:
        tempA[i] += 1
    for i in arrB:
        tempB[i] += 1

    for i in range(4, 0, -1):
        if tempA[i] > tempB[i]:
            result = 'A'
            break
        elif tempA[i] < tempB[i]:
            result = 'B'
            break
        else:
            result = 'D'
    print(result)