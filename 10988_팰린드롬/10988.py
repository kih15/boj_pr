import sys
sys.stdin = open('input.txt')

s = input()
res = 0
if s == s[::-1]:
    res = 1
print(res)


