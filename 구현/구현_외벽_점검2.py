# 14 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i]+n)

    dist.sort(reverse = True)
    answer = len(dist) + 1
    for i in range(length) :
        for friend in permutations(dist, len(dist)) :
            now = weak[i] + friend[0]
            count = 1
            for index in range(i+1, i+length) :
                if now < weak[index] :
                    count += 1
                    if count > len(dist) : break
                    now = weak[index] + friend[count-1]
            answer = min(answer, count)
    return -1 if answer > len(dist) else answer

if __name__ == "__main__" :
    solution(12, [1, 5, 6, 10], [1, 2, 3, 4])



