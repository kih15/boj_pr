import sys
sys.stdin = open('input.txt')

n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

# print(data)
# x, y 가 둘 다 커야한다.
# 하나만 크다면 같은 그룹으로 묶기

# sort_data = sorted(data, key=lambda x: (x[0], x[1]))
# print(sort_data)

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")