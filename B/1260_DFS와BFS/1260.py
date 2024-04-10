import sys
sys.stdin = open('input.txt')

def dfs(s):
    for to in adjl[s]:
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)

def bfs(s):
    q = [s]
    visited[s] = 1

    while q:
        path1 = q.pop(0)
        print(path1, end=' ')

        for to in adjl[path1]:
            if visited[to]:
                continue

            visited[to] = 1
            q.append(to)


N, M, V = map(int, input().split())
adjl = [[] for _ in range(M + 1)]
visited = [0] * M
path = []
path1 = []
for i in range(M):
    s, e = map(int, input().split())
    adjl[s].append(e)
    adjl[e].append(s)

visited[V] = 1
path.append(V)
dfs(V)
res = path
print(res)

bfs(V)
ans = path1
print(ans)
