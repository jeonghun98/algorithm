'''서로소 집합을 활용한 사이클 판별 소스코드'''
import os
os.system('chcp 65001')

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선의 개수 입력
v, e = map(int,input().split())
parent = [0] * (v + 1)

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1) :
    parent[i] = i

cycle = False
for i in range(e) :
    a, b = map(int, input().split())
    if find_parent(parent,a) == find_parent(parent, b) :
        cycle = True
        break
    else :
        union_parent(parent, a, b)

if cycle :
    print('사이클이 발생했습니다.')
else :
    print('사이클이 발생하지 않았습니다.')