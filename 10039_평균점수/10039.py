import sys
sys.stdin = open('input.txt')

sum_v = 0
for _ in range(5):
    s = int(input())
    if s >= 40:
        s = s
    else:
        s = 40
    sum_v += s
avg = sum_v // 5
print(avg)