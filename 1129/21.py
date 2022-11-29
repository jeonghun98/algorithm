# 21 인구 이동
import sys
input = sys.stdin.readline

from collections import deque
n, l, r = map(int, input().split())
data = []
for _ in range(n) :
    data.append(list(map(int, input().split())))

def bfs(i,j,id) :
    temp = [[i,j]]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((i,j))
    union[i][j] = id
    count = 1
    num_s = data[i][j]
    while q :
        x,y = q.popleft()
        now = data[x][y]
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n : continue
            if l <= abs(now - data[nx][ny]) <= r:
                if union[nx][ny] == 0 :
                    q.append((nx, ny))
                    union[nx][ny] = id
                    count += 1
                    num_s += data[nx][ny]
                    temp.append((nx,ny))

    for i, j in temp :
        data[i][j] = int(num_s/count)

result = 0
while True :
    union = [[0] * n for _ in range(n)]

    id = 1
    for i in range(n) :
        for j in range(n) :
            if union[i][j] == 0 :
                bfs(i,j, id)
                id += 1
    if id - 1 == (n*n):
        break
    result += 1
    # for i in range(n) :
    #     for j in range(n) :
    #         print(data[i][j], end = " ")
    #     print()
print(result)