'''최종 순위'''
from collections import deque

for tc in range(int(input())) :
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for _ in range(n+1)] # n+1 x n+1

    data = list(map(int, input().split()))

    for i in range(n) :
        for j in range(i+1, n) :
            graph[data[i]][data[j]] = True # 5 4 3 2 1 -> 5>4, 5>3, 5>2, 5>1
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m) :
        a, b = map(int, input().split())

        if graph[a][b] : # a -> b 였다면
            graph[a][b] = False # 0 x n+1로 하면 append와 delete 때문에 불편함
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else :          # b -> a 였다면
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)

    certain = True
    cycle = False

    for i in range(n) : #1개씩 n번 반복 -> n개의 result
        if len(q) == 0 :
            cycle = True
            break
        if len(q) >= 2 :
            certain = False
            break
        now = q.popleft()
        result.append(now)

        for j in range(1,n+1) :
            if graph[now][j] :
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle :
        print("IMPOSSIBLE")
    elif not certain :
        print("?")
    else :
        for i in result :
            print(i, end = " ")
        print()