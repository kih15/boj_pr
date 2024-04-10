import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return fib(n-1) + fib(n-2)

def fibo(n):
    global cnt2
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
        cnt2 += 1
    return f[n]

n = int(input())
cnt1 = 1
cnt2 = 0
fib(n)
fibo(n)
print(cnt1, cnt2)
