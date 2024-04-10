N = int(input())
cnt = 0
a = b = 0
min_v = 0

if 3 * a + 5 * b == N:
    cnt = a + b
    if min_v > cnt:
        min_v = cnt
    print(min_v)
else:
    print(-1)
