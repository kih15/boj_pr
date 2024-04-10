import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    k = int(input()) # 층
    n = int(input()) # 호
    zero = [0] * (n+1)
    for i in range(1, n+1): # 0층 주민
        zero[i] += i

    for i in range(k):
        for j in range(1, n):
            zero[j+1] += zero[j]
    print(zero[-1])

# 1층의 3호에 살려면 0층의 1호부터 3호까지 총 사람수 6
# 01 = 1 02 = 2 03 = 3
# 2층의 3호에 살려면 1층의 1호부터 3호까지 총 사람수
# 11 = 1 12 = 3 13 = 6
# 21 = 1 22 = 4 23 = 10