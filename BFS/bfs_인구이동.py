'''인구 이동'''
from collections import deque

n, l, r = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    united = []
    united.append([x, y])

    count = 1
    num = data[x][y]

    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            now = data[i][j]
            nx = dx[k] + i
            ny = dy[k] + j
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                next = data[nx][ny]
                if l <= abs(now - next) <= r:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    count += 1
                    num += next
                    united.append([nx, ny])

    # 방문했던 곳을 바꾸면 전에 방문했던 곳(visited)도 다시 재할당되기 때문에
    # 현재 dfs에서 방문했던 곳(united)만 재할당
    for i, j in united:
        data[i][j] = int(num / count)

result_count = 0
while True:
    visited = [[False] * n for i in range(n)]
    bfs_count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                bfs_count += 1

    if bfs_count == n * n:
        break

    result_count += 1

print(result_count)