# 13 치킨 배달
from itertools import combinations

def distance(home, chicken) :
    total = 0
    for i in home :
        x, y = i
        temp = (n-1)*2
        for j in chicken :
            cx, cy = j
            temp = min(temp, abs(x-cx) + abs(y-cy))
        total += temp
    return total

n, m = map(int, input().split())
home = []
chicken = []

for i in range(n) :
    data = list(map(int, input().split()))
    for j in range(n) :
        if data[j] == 1 : home.append((i,j))
        if data[j] == 2 : chicken.append((i,j))

result = (n-1)*2*len(home)
if m == len(chicken) :
    result = distance(home, chicken)
else :
    for i in combinations(chicken, m) :
        result = min(distance(home, i), result)

print(result)
