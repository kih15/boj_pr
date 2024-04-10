import sys
sys.stdin = open('input.txt')
def facto(s):
    if s == 1:
        return s
    return s * facto(s-1)
n = int(input())
res = str(facto(n))
print(res)
cnt = 0
for i in res:
    if res[len(res)] == 0:
        cnt += 1
print(cnt)