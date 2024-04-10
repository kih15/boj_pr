import sys
sys.stdin = open('input.txt')

N = int(input())
p = list(map(int, input().split()))
p.sort()
# print(p)
sum_v = 0
res = 0
for i in p:
    sum_v += i
    res += sum_v
print(res)