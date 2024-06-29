import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
arr = []
yose = []
n, k = map(int, input().split())
for i in range(1, n+1):
    arr.append(i)
while len(arr) != 0:
    print(arr[(3*i-1)%n])
    yose.append(arr[(3*i-1) % n])
print(yose)