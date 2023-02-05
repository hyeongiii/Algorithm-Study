import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

cnt = 0

# DFS를 이용하여 방문한 곳은 1로 처리
def dfs(r, c):
    # 만약 r, c 값이 얼음판의 범위를 벗어날 경우 False 반환
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    # 현재 노드를 아직 방문하지 않은 경우
    if graph[r][c] == 0:
        graph[r][c] = 1
        # 상하좌우 위치들도 재귀적으로 호출
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        return True
    return False


for r in range(n):
    for c in range(m):
        if dfs(r, c):
            cnt += 1

print(cnt)