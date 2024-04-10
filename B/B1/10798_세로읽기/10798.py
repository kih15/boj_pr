import sys
sys.stdin = open('input.txt')

arr = [input() for _ in range(5)]
res = ''
# print(arr)
for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            res += arr[j][i]
print(res)
