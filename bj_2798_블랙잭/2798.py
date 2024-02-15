import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# N장의 카드 중에서 3장을 골라서 M을 넘지 않으면서 최대한 가깝게
# 초과만 안하면 된다.

max_sum = 0
sum_v = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_v = arr[i] + arr[j] + arr[k]
            if sum_v <= M:
                if max_sum < sum_v:
                    max_sum = sum_v
print(max_sum)