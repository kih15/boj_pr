import sys
sys.stdin = open('input.txt')

def middle_value(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

a, b, c = map(int, input().split())
s = input()

A = min(a, b, c)
B = middle_value(a, b, c)
C = max(a, b, c)

values = {'A': A, 'B': B, 'C': C}
result = " ". join(str(values[char]) for char in s)
print(result)