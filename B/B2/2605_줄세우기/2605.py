import sys
sys.stdin = open('input.txt')

N = int(input())
temp = [0] * N
arr = list(map(int, input().split()))
for i in range(1, N+1):
    temp[i-arr[i-1]:] = temp[i-arr[i-1]-1:-1]
    temp[i-arr[i-1]-1] = i
print(*temp)
# stack = []
# line = ''
# for i in arr:
#     if arr[i] == 0:
#         line += str(arr[i])
#     elif arr[i] ==

    #     stack.append(i)
    #     continue
    # if stack[-1] < arr[i]:
    #     line += str(stack.pop())
