import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
board = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            board[i][j] = 'w'



            
