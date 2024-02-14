import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
stack = []
line = ''
for i in arr:
    if not stack:
        stack.append(i)
        continue
    if stack[-1] < arr[i]:
        line += str(stack.pop())
    stack.append(i)
    print(line)
