from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value) :
    left_i = bisect_left(array, left_value)
    right_i = bisect_right(array, right_value)
    return right_i - left_i

#각 단어 길이는 10000개 이하로 나옴 -> 1~10000개의 길이를 가진 리스트들의 리스트 -> array[500] : 길이가 500인 단어의 리스트
array = [[] for _ in range(10001)]
reverse_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
    for i in range(10001) :
        array[i].sort()
        reverse_array[i].sort()
    for q in queries :
        if q[0] != '?' : #접미사가 와일드카드 -> fro?? -> froaa부터 frozz 넣을 index의 차이 구하기
            res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?', 'z'))
        else : #접두사에 와일드카드 -> ????o -> o???? -> 위와 동일
            res = count_by_range(reverse_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)
    return answer

if __name__ == "__main__" :
    print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))