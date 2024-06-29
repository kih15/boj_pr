import sys
sys.stdin = open('input.txt')

m = input()
split_m = m.split('|')
a = 0
c = 0
for i in split_m:
    if i[0] in ('A', 'D', 'E'):
        a += 1
    elif i[0] in ('C', 'F', 'G'):
        c += 1

if a > c:
    print('A-minor')
elif a < c:
    print('C-major')
else:
    if split_m[-1][-1] in ('A', 'D', 'E'):
        print('A-minor')
    elif split_m[-1][-1] in ('C', 'F', 'G'):
        print('C-major')