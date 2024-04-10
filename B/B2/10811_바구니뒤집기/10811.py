import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
bag = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    temp = bag[i-1:j]
    temp.reverse()
    bag[i-1:j] = temp
print(*bag)
