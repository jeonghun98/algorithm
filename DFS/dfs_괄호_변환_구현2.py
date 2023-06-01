# 18 괄호 변환

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
    for i in p:
        if i == "(":
            count += 1
        else:
            count -= 1
            if count < 0 :
                return False
    return True

def solution(p):
    if p == "" :
        return p
    index = balance(p)
    u = p[0:index+1]
    v = p[index+1:]
    if check(u) :
        answer = u + solution(v)
    else :
        answer = "("
        answer += solution(v)
        answer += ")"
        temp = list(u[1:-1])
        for i in range(len(temp)) :
            if temp[i] == "(" :
                temp[i] = ")"
            else :
                temp[i] = "("
        answer += ''.join(temp)
    return answer

