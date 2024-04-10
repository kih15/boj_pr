import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
tmp = []
for _ in range(n):
    num = int(input())
    tmp.append(num)
tmp.sort()
for i in tmp:
    print(i)