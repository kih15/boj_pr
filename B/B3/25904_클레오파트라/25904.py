import sys
sys.stdin = open('input.txt')

n, x = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
while True:
    c = cnt % n
    voice = x + cnt
    if voice > arr[c]:
        print(c+1)
        break
    cnt += 1