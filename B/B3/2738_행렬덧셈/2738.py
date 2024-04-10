import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()

# a = []
# b = []
# N, M = map(int, input().split())
# for i in range(N):
#     A = list(map(int, input().split()))
#     a.append(A[i])
# for i in range(M):
#     B = list(map(int, input().split()))
#     b.append(B[i])
#     print(a)
#     print(b)