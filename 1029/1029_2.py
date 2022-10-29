'''탑승구'''
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

g = int(input())
p = int(input())
parking = [0] * (g+1)

for i in range(1, g+1) :
    parking[i] = i

result = 0
stop = False
for _ in range(p) :
    data = find_parent(parking, int(input()))
    if data == 0 or stop:
        stop = True
        continue
    union_parent(parking, data, data-1)
    result += 1

print(result)
#print(parking)