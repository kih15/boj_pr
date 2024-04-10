import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
arr = []
for tc in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()
for i in range(n):
    print(arr[i][0], arr[i][1])