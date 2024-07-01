import sys
sys.stdin = open('input.txt')
import math

n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    gcd = math.gcd(arr[i], arr[0])

    a = arr[i] // gcd
    b = arr[0] // gcd

    print(f"{b}/{a}")