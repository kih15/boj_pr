import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])//arr[0]
    # print(avg)
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] > avg:
            cnt += 1
    res = cnt / (len(arr)-1)

    print(f'{format((res*100), ".3f")}%')