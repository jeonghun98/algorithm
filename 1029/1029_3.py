'''어두운 길'''

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n)

edges = []
result = 0

for i in range(n) :
    parent[i] = i

for i in range(m) :
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges :
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
    else :
        result += cost

print(result)