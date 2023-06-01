'''개선된 다익스트라 알고리즘 소스코드'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드와 간선의 개수 입력
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    #시작 노드로 가기 위해 최단경로를 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        # 가장 최단 거리가 짧은 노드에 대한 정보
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다르 노드로 이동하는 거리가 더 짧은 경우 -> 리스트 갱신 후 큐에 삽입
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INFINITY")
    else:
        print(distance[i])



