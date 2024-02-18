arr = list(map(int, input().split()))
sum_v = 0
for i in arr:
    sum_v += i ** 2
print(sum_v % 10)