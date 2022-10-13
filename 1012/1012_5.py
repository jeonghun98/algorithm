'''실패율'''

def solution(N, stages):
    length = len(stages)
    stages.sort()
    answer = []

    for i in range(1, N + 1):
        num = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = num / length
        length -= num
        answer.append((i, fail))

    #x : -x[1] or x : (-x[1], x[0]) -> x[0]은 이미 오름차순이라서 상관 x
    print(answer)
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    print(answer)
    answer = [i[0] for i in answer]

    return answer

def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    print(result)
    return sorted(result, key=lambda x : result[x], reverse=True)

if __name__ == '__main__' :
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4, 4, 4, 4, 4]))