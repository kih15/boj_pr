import sys
sys.stdin = open('input.txt')

N = int(input())
x = 0
for i in range(N):
    a = list(map(int, str(i)))
    if N == sum(a) + i:
        x = i
        break
print(x)
# sum1 = 0
# for i in str(N):
#     sum1 += int(i)
#     hap = N + sum1
#     if hap == N:
#         print(i)
#         break
# print(hap)
