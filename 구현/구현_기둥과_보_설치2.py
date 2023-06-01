# 12 기둥과 보 설치
def possible(answer) :
    for i in answer :
        x,y,a = i
        if a == 0 : # 기둥
            if y == 0 : continue # 바닥 위
            if [x,y-1,0] in answer : continue # 다른 기둥 위
            if [x-1,y,1] in answer or [x,y,1] in answer : continue # 보의 한쪽 끝 위
            return False
        else :      # 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer: continue # 한쪽 끝 부분이 기둥 위
            if [x-1,y,1] in answer and [x+1,y,1] in answer : continue # 양쪽 끝 부분이 다른 보와 동시 연결
            return False
    return True

def solution(n, build_frame):
    answer = []
    for i in build_frame :
        x,y,a,b = i
        if b == 0 :
            answer.remove([x,y,a])
            if not possible(answer) :
                answer.append([x, y, a])
        else :
            answer.append([x,y,a])
            if not possible(answer) :
                answer.remove([x,y,a])

    return sorted(answer)

if __name__ == "__main__" :
    n = 5
    build_frame =[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
    print(solution(n, build_frame))