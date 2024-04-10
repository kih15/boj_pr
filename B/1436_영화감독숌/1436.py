import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = 0
result = 666
while True:
    if '666' in str(result):
        cnt += 1
    if N == cnt:
        break
    result += 1
print(result)