import sys
sys.stdin = open('input.txt')


def f(arr, N):
    max_v = 0
    for i in range(N):
        s = 0
        for j in range(i, N):
            # 0 ~ N까지
            # 1 ~ N까지 ...
            # if j + 1 < N and arr[j+1] + arr[j] < 0:
            #     continue
            s += arr[j]
            if s > max_v:
                temp.append(s)
                # print(temp)
    return max(temp)
n = int(input())
arr = list(map(int, input().split()))
temp = []
# print(f(arr, n))
# print(temp)

for i in range(1, n):
    arr[i] = max(arr[i], arr[i]+arr[i-1])
print(max(arr))