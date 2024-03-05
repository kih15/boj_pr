import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
bag = []
for x in range(N):
    bag.append(x+1)
# print(bag)
for _ in range(M):
    i, j = map(int, input().split())
    # print(i, j)
    bag[i-1], bag[j-1] = bag[j-1], bag[i-1]
print(*bag)
