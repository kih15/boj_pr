import sys
sys.stdin = open('input.txt')
a = []
b = []
N, M = map(int, input().split())
for i in range(N):
    A = list(map(int, input().split()))
    a.append(A[i])
for i in range(M):
    B = list(map(int, input().split()))
    b.append(B[i])
    print(a)
    print(b)