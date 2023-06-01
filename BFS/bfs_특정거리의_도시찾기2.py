# 15 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
data = [[] for _ in range(n+1)]
dis = [-1] * (n+1)
for _ in range(m) :
    s, e = map(int, input().split())
    data[s].append(e)

def bfs(start) :
    dis[start] = 0
    q = deque()
    q.append(start)
    while q :
        now = q.popleft()
        for i in data[now] :
            if dis[i] == -1:
                q.append(i)
                dis[i] = dis[now] + 1

bfs(x)

if dis.count(k) == 0 :
    print(-1)
else :
    for i,d in enumerate(dis) :
        if d == k: print(i)