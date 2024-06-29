import sys
sys.stdin = open('input.txt')

num = 0
for _ in range(5):
    n = int(input())
    num += n
print(num)