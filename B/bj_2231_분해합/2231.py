import sys
sys.stdin = open('input.txt')

N = int(input())
x = 0
for i in range(N):
    sum1 = i
    for j in str(i):
        sum1 += int(j)
    if sum1 == N:
        x = i
        break
print(x)
