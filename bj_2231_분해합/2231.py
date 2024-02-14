import sys
sys.stdin = open('input.txt')

N = int(input())
sum1 = 0
for i in str(N):
    sum1 += int(i)
    hap = N + sum1
    if hap == N:
        print(i)
        break
else:
    print(0)