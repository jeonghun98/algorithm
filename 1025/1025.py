'''숨바꼭질'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
start = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF] * (n+1)
distance[0] = 0



def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(start)

# value = max(distance)
# count = distance.count(value)
# index = distance.index(value)
# print(index, value, count)

max_node = 0
max_distance = 0
result = []

for i in range(1, n+1) :
    if max_distance < distance[i] :
        max_node = i
        max_distance = distance[i]
        result = [i]
    elif max_distance == distance[i] :
        result.append(i)
print(max_node, max_distance, len(result))
