import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
cnt = list(map(int, input().split()))
count = 0
for i in cnt:
    if i in arr:
        count += 1
print(count)

