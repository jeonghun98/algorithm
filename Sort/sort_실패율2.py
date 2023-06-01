# 25 실패율

def solution(N, stages):
    total = len(stages)
    temp = []
    for i in range(1, N + 1):
        num = stages.count(i)
        if total == 0 : fail = 0
        else : fail = num / total
        temp.append((i, fail))
        total -= num
    temp.sort(key=lambda x: (-x[1],x[0]))
    result = [i[0] for i in temp]

    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
