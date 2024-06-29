import sys
sys.stdin = open('input.txt')

def c_rank(n, k, countries):
    countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    rank = 1
    for i in range(n):
        if countries[i][0] == k:
            t = countries[i]
            break

    for i in range(n):
        if countries[i][1:] == t[1:]:
            break
        rank += 1

    return rank
n, k = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

print(c_rank(n, k, countries))
