import sys
sys.stdin = open('input.txt')

def op(a, b):
    return (a+b)*(a-b)

input = sys.stdin.readline
a, b = map(int, input().split())

res = op(a, b)
print(res)