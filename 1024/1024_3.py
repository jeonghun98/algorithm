'''플로이드 워셜 알고리즘 소스코드'''
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 가는 비용 0으로 초기화
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            graph[a][b] = 0

#각 간선에 정보 입력받아, 리스트 초기화
for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) :
    for a in range(1,n+1) :
        for b in range(1,n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1) :
    for b in range(1,n+1) :
        if graph[a][b] == INF :
            print("INFINITY", end = " ")
        else :
            print(graph[a][b], end = " ")
    print()