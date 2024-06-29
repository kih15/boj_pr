import sys
sys.stdin = open('input.txt')


def d(n):
    total = n
    while n > 0:
        total += n % 10
        n //= 10
    return total

def find_selfnum(limit):
    has_generator = [False] * (limit + 1)

    for i in range(1, limit + 1):
        dn = d(i)
        if dn <= limit:
            has_generator[dn] = True

    self_numbers = [i for i in range(1, limit + 1) if not has_generator[i]]
    return self_numbers


# 10000보다 작거나 같은 셀프 넘버를 출력
limit = 10000
self_numbers = find_selfnum(limit)

for num in self_numbers:
    print(num)