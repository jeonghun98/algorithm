from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    data[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = 0
                q.append((nx, ny))


T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)