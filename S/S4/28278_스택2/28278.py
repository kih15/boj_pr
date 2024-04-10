import sys
sys.stdin = open('input.txt')

stack = []
N = int(sys.stdin.readline())
for tc in range(1, N+1):
    x = sys.stdin.readline()
    if x[0] == '1':
        stack.append(int(x[2:]))
    if x[0] == '2':
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    if x[0] == '3':
        print(len(stack))
    if x[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if x[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
