'''치킨 배달'''

from itertools import combinations

def get_sum(data1, data2) :
    result = 0
    for hx, hy in data1 :
        temp = 1e9
        for cx, cy in data2 :
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

    # 해당 코트는 data1 루프를 돌때 temp를 초기화 못 시키므로 삭제
    # temp = 1e9
    # result = sum([min(temp, abs(hx-cx)+abs(hy-cy)) for cx, cy in data2 for hx, hy in data1])

n, m = map(int, input().split())
list_2 = []
list_1 = []

for r in range(n) :
    data = (list(map(int, input().split())))
    for c in range(n):
        if data[c] == 2:
            list_2.append([r, c])
        elif data[c] == 1:
            list_1.append([r, c])

if len(list_2) > m :
    com_2 = list(combinations(list_2, m))
    result = 1e9
    for com in com_2 :
        result = min(get_sum(list_1, com), result)
    print(result)
else :
    print(get_sum(list_1, list_2))

