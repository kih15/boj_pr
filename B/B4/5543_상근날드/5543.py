import sys
sys.stdin = open('input.txt')

set_menu = []
for _ in range(5):
    n = int(input())
    set_menu.append(n)

price = min(set_menu[:3]) + min(set_menu[3:])
print(price-50)
