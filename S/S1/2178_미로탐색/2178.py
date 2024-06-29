import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

queue = [(0, 0)]
maze[0][0] = 1

while queue:
    i, j = queue.pop(0)

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1:
            maze[ni][nj] = maze[i][j] + 1
            queue.append((ni, nj))

print(maze[n-1][m-1])