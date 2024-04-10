import sys
sys.stdin = open('input.txt')

n = input()
arr = []
num = ''
for i in n:
    arr.append(i)
    arr.sort(reverse=True)
for i in arr:
    num += i
print(int(num))


