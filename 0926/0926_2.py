'''프로그래머스 - 외벽 점검'''
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start + 1, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

if __name__ == "__main__" :
    print(solution(12,[1,5,6,10],[1,2,3,4]))