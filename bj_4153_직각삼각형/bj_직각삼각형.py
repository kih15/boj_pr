import sys
sys.stdin = open('input.txt')

while True:
    a, b, c = map(int, input().split())
    if a == 0 or b == 0 or c == 0:
        break
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print('right')
    else:
        print('wrong')