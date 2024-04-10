import sys
sys.stdin = open('input.txt')

n = int(input())
line = list(map(int, input().split()))
stack = []
# line에 있는 값들을 순서대로 stack에 넣는다.
# 1부터 차례대로 pop해서 stack에 넣었다가 pop 할 수 있으면
# Nice 출력 못하면 Sad 출력
res = "Sad"
target = 1
for i in line:
    stack.append(i)
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
    if len(stack) > 1 and stack[-1] > stack[-2]:
        res = "Sad"
if stack:
    print(res)
else:
    print('Nice')
