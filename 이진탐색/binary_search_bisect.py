'''정렬된 배열에서 특정 수의 개수 구하기 - 시간 복잡도 O(logN)'''
'''bisect 라이브러리 사용'''

from bisect import bisect_left, bisect_right

def count_by_value(array, left_value, right_value) :
    right_i = bisect_right(array,right_value)
    left_i = bisect_left(array,left_value)
    # print(right_i, left_i)
    return right_i - left_i

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x, x)

if count == 0 : print(-1)
else : print(count)
