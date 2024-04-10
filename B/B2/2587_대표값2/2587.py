import sys
sys.stdin = open('input.txt')

arr = []
for _ in range(5):
    n = int(input())
    arr.append(n)

arr.sort()
avg = sum(arr)//len(arr)
print(avg)
print(arr[len(arr)//2])
