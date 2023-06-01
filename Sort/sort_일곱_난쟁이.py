# 일곱 난쟁이
from itertools import combinations
data = []
for _ in range(9) :
    data.append(int(input()))

for i in combinations(data, 7) :
    if sum(i) == 100 :
        result = list(i)
        break

result.sort()

for i in result :
    print(i)