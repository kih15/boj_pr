import sys
sys.stdin = open('input.txt')
# from itertools import combinations
n, m = map(int, input().split())
num = list(map(int, input().split()))

# max_v = 0
# res = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             max_v = num[i] + num[j] + num[k]
#             if max_v <= m:
#                 if res < max_v:
#                     res = max_v
# print(res)

# res = 0
# for combo in combinations(num, 3):
#     combo_sum = sum(combo)
#     if combo_sum <= m and combo_sum > res:
#         res = combo_sum
#
# print(res)

num.sort()

res = 0
for i in range(n-2):
    if num[i] > m:
        break
    for j in range(i+1, n-1):
        if num[i] + num[j] > m:
            break
        for k in range(j+1, n):
            current_sum = num[i] + num[j] + num[k]
            if current_sum > m:
                break
            if current_sum > res:
                res = current_sum

print(res)