import sys
sys.stdin = open('input.txt')

s = input()
if s[0] == '"' and s[-1] == '"':
    if s[1:-1] == '':
        print('CE')
    print(s[1:-1])

else:
    print('CE')
