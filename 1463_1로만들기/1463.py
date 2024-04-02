import sys
sys.stdin = open('input.txt')

N = int(input())
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# => 이를 활용해서 1을 만든다 연산을 사용하는 횟수의 최솟값을 출력하라
# cnt = 0
# while N > 1:
#     if N % 3 == 0:
#         N = N / 3
#         cnt += 1
#     elif N % 2 == 0:
#         N = N / 2
#         cnt += 1
#     else:
#         N = N - 1
#         cnt += 1
# print(cnt)

d = [0] * (N+1)
for i in range(2, N+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
print(d[N])