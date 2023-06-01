# 5-11 (4 미로탈출)
from collections import deque

n, m = map(int, input().split())
gr = []
for _ in range(n) :
    gr.append(list(map(int, input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    x0, y0 = x,y
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == x0 and ny == y0 : continue #경로 확인을 위해 추가로 넣음
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if gr[nx][ny] == 0 :
                continue
            if gr[nx][ny] == 1 :
                gr[nx][ny] = gr[x][y] + 1
                q.append((nx, ny))
                if nx == n-1 and ny == m-1 : #최단경로 발견 후 break
                    q.clear()
                    break
    return gr[n-1][m-1]

print(bfs(0,0))
for i in range(n) :
    for j in range(m) :
        print(gr[i][j], end= " ")
    print()