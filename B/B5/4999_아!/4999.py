import sys
sys.stdin = open('input.txt')

me = len(input())
doc = len(input())
if me >= doc:
    print('go')
else:
    print('no')