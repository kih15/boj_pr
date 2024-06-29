import sys
sys.stdin = open('input.txt')

n, m, v = map(int, input().split())
visited = [0] * (n+1)
visited.sort()
path = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
def dfs(now):

    for to in graph[now]:
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)

visited[v] = 1
path.append(v)
dfs(v)
print(*path)
def bfs(start):
    queue = [start]
    visited1[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        for to in graph[now]:
            if visited1[to]:
                continue

            visited1[to] = 1
            queue.append(to)
visited1 = [0] * (n+1)
visited1.sort()
bfs(v)
