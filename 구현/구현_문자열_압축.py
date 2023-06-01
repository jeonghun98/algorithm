# 09 문자열 압축
def solution(s):
    length = len(s)
    result = length
    for i in range(1, length // 2 + 1) :
        string = ""
        bef = s[0:i]
        count = 1
        for j in range(i,length, i) :
            now = s[j : j+i]
            if bef == now :
                count += 1
            else :
                string += str(count) + bef if count > 1 else bef
                count = 1
                bef = now
        string += str(count) + bef if count > 1 else bef

        # 이중 for문 range변경 -> string은 끝의 index범위 넘어도 가능
        # if length % i != 0 :
        #     string += s[(length//i)*i : ]

        #print(string)
        result = min(len(string), result)
    return result

if __name__ == "__main__" :
    print(solution(input()))