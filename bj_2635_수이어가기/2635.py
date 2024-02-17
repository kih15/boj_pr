import sys
sys.stdin = open('input.txt')

N = int(input())
max_len = 0
result = []
for i in range(1, N+1):
    lst = [N]
    lst.append(i)
    while lst[-2] - lst[-1] >= 0:
        max_idx = lst[-2] - lst[-1]
        lst.append(max_idx)

        if max_len < len(lst):
            max_len = len(lst)
            result = lst

print(max_len)
print(*result)