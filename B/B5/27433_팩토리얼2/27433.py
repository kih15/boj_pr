import sys
sys.stdin = open('input.txt')

def facto(n):
    if n <= 1:
        return 1
    elif n > 1:
        return n * facto(n-1)

input = sys.stdin.readline
n = int(input())

num = facto(n)
print(num)


