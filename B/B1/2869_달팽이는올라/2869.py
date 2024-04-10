import sys
sys.stdin = open('input.txt')

A, B, V = map(int, input().split())
i = 0 # 일 수
# 하루에 1씩 올라가지만 마지막에 오를땐 100
if (V-A) % (A-B) == 0:
    print(int((V-B)/(A-B)))
else:
    print(int(((V-B)/(A-B))+1))
# while True:
#     i += 1
#     if A*i - B*(i-1) >= V:
#         break
# print(i)
# 하루에 1씩 올라가지만 마지막에 오를땐 100
