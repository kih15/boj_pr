import sys
sys.stdin = open('input.txt')

arr = []
sum_v = 0
N = 9
for i in range(N):
    n = int(input())
    arr.append(n)
    sum_v += n  # 아홉 난쟁이 키의 총합은 140
arr.sort()
n1 = 0
n2 = 0
for i in range(N):
    for j in range(i+1, N):
        if sum_v - (arr[i] + arr[j]) == 100:
            n1 = arr[i]
            n2 = arr[j]
            break

arr.remove(n1)
arr.remove(n2)

for i in arr:
    print(i)


