import sys
sys.stdin = open('input.txt')

def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


a, b = map(int, input().split()) # 가로, 세로
n = int(input()) # 칼로 자른 수
lst_a = [0, a] # 잘랐을 때 길이를 만들어주기 위해
lst_b = [0, b]

for _ in range(n):
    x, y = map(int, input().split())
    if x == 0:
        lst_b.append(y)
    else:
        lst_a.append(y)

bubblesort(lst_b)
bubblesort(lst_a)
max_width = 0
max_height = 0
for i in range(len(lst_b)-1):
    height = lst_b[i+1] - lst_b[i]
    if max_height < height:
        max_height = height
for i in range(len(lst_a)-1):
    width = lst_a[i+1] - lst_a[i]
    if max_width < width:
        max_width = width

answer = max_width * max_height
print(answer)
