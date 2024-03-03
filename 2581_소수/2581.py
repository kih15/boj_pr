M = int(input())
N = int(input())
lst = []
min_v = 10001
for i in range(M, N+1):
    cnt = 0
    for j in range(2, N):
        if i % j != 0:
            cnt = i

        if min_v > i:
            min_v = i
    print(cnt)
print(min_v)

