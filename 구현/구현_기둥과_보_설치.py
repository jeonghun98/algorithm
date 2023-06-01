'''기둥과 보 설치'''

def possible(answer):
    for i in answer:
        x, y, a = i
        # 기둥
        # 바닥 위 or 보의 한쪽 끝 위 or 다른 기둥 위
        if (a == 0):
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        # 보
        # 한쪽 끝이 기둥 위 or 양쪽 끝이 다른 보와 연결
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, a, b = i
        # 삭제
        if (b == 0):
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        # 설치
        else:
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
    return sorted(answer)

if __name__ == "__main__" :
    a = [5, 5]
    b = [[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]],
                   [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                    [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]] ]
    for x, y in zip(a, b):
        print(solution(x, y))