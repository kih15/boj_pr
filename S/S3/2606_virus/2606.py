import sys
sys.stdin = open('input.txt')

def dfs(s):
    # cnt를 전역 변수로 사용
    global cnt
    # 현재 노드 s의 인접 노드를 순회
    for to in adjl[s]:
        # 이미 방문한 노드는 건너뜀
        if visited[to]:
            continue
        # 방문하지 않은 노드를 방문 처리
        visited[to] = 1
        # 경로에 추가 (디버깅용, 실제 로직에는 필요 없음)
        path.append(to)
        # 감염된 컴퓨터 수 증가
        cnt += 1
        # 재귀적으로 DFS 수행
        dfs(to)

# 입력
v = int(input()) # 컴퓨터(노드)의 수
e = int(input()) # 간선의 수

# 방문 체크 리스트 초기화 (모든 노드를 방문하지 않은 상태로 초기화)
visited = [0] * (v+1)
# 경로 기록 리스트 (디버깅용)
path = []
# 감염된 컴퓨터 수를 세기 위한 변수 초기화
cnt = 0

# 인접 리스트 초기화 (그래프 초기화)
adjl = [[] for _ in range(v+1)]

# 간선 정보 입력 받아서 그래프 구성
for _ in range(e):
    a, b = map(int, input().strip().split())
    adjl[a].append(b)
    adjl[b].append(a)

# print(adjl)

# 1번 컴퓨터를 방문 처리하고 DFS 시작
visited[1] = 1
path.append(1)
dfs(1)

# 결과
print(cnt)