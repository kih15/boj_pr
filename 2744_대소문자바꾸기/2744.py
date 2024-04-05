import sys
sys.stdin = open('input.txt')

s = input()
res = ''
for i in s:
    if i.isupper():
        i = i.lower()
        res += i
    else:
        i = i.upper()
        res += i
print(res)