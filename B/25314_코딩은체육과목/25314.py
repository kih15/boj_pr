import sys
sys.stdin = open('input.txt')

N = int(input())
n = N//4
print('long '* n + 'int')