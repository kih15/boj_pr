import sys
sys.stdin = open('input.txt')

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    GCD = gcd(A, B)
    print(A*B//GCD)