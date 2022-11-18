# 바이러스
from collections import deque
def bfs(graph, start, visited) :
    visited[start] = True
    q = deque()
    q.append(start)
    count = 0
    while q :
        now = q.popleft()
        for i in graph[now]:
            if not visited[i] :
                visited[i] = True
                q.append(i)
                count += 1
    return count

def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v]:
        if not visited[i] :
            dfs(graph, i, visited)

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
for _ in range(e) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#result = bfs(graph,1,visited)
#print(result)

dfs(graph,1,visited)
print(visited.count(True) - 1)