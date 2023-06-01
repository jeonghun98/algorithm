'''경쟁적 전염'''
from collections import deque

n, k = map(int, input().split())
data = []
virus = []

for i in range(n) :
    data.append(list(map(int, input().split())))
    for j in range(n) :
        if data[i][j] != 0 :
            virus.append([data[i][j], 0, i, j])


# sorted(virus) -> return 만 sort
# virus.sort() -> return x, virus sort
virus.sort()
q = deque(virus)

s, x, y = map(int, input().split())

# 북쪽부터 시계방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

time = 0
while q :
    v, time, i, j = q.popleft()
    if time == s :
        break
    for k in range(4) :
        nx = dx[k] + i
        ny = dy[k] + j
        if nx < n and nx >= 0 and ny < n and ny >= 0 :
            if data[nx][ny] == 0 :
                data[nx][ny] = v
                q.append([data[nx][ny], time + 1, nx, ny])

print(data[x-1][y-1])