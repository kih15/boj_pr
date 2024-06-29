import sys
sys.stdin = open('input.txt')
from collections import Counter

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    n = int(input())
    arr.append(n)
arr.sort()

# 산술평균인데 소수점 첫째 자리에서 반올림
print(round(sum(arr)/N))

# 중앙값
print(arr[len(arr)//2])

# 최빈값인데 여러개 있으면 최빈값 중 두 번째로 작은 값
cnt = Counter(arr).most_common(2)
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 범위
print(max(arr)-min(arr))
