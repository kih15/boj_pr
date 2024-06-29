import sys
sys.stdin = open('input.txt')

s = input()
stack = []
for i in s:
    if i == '*/+-':

