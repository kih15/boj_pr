import sys
sys.stdin = open('input.txt')

T = int(input())
book = dict()
for tc in range(1, T+1):
    name = input()
    # print(s)
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
max = 0
sbook = dict(sorted(book.items()))
for i in sbook:
    if sbook[i] > max:
        max = sbook[i]
        res = i
print(res)
