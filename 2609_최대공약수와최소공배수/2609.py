import sys
sys.stdin = open('input.txt')

N = 10000
a, b = map(int, input().split())
GCD = 0 # 최대공약수
LCM = 0 # 최소공배수
for i in range(1, N+1):
    if a % i == 0 and b % i == 0:
        if GCD < i:
            GCD = i
    LCM = a * b // GCD
print(GCD)
print(LCM)