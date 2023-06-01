def balance(p) :
    count = 0
    for i in range(len(p)) :
        if p[i] == "(" :
            count += 1
        else :
            count -= 1
        if count == 0 :
            return i

def check(p) :
    count = 0
    for i in p :
        if i == "(" :
            count += 1
        else :
            if count == 0 :
                return False
            count -= 1
    return True

def solution(p):
    answer = ""
    if p == "" :
        return p
    index = balance(p)
    u = p[:index+1]
    v = p[index + 1:]
    if check(u) :
        answer = u + solution(v)
    else :
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)) :
            if u[i] == "(" :
                u[i] = ")"
            else :
                u[i] = "("
        answer += "".join(u)
        #"".join(리스트) -> 리스트를 문자열로 반환
    return answer

if __name__ == "__main__" :
    print(solution("()))((()"))