'''선택 정렬 소스코드'''
array  = [7,5,9,0,3,1,6,2,4,8]

#i는 정렬 완
for i in range(len(array)) :
    min_index = i
    for j in range(i+1,len(array)) :
        if array[min_index] > array[j] :
            min_index = j
        array[min_index], array[i] = array[i], array[min_index]
print(array)

'''삽입 정렬 소스코드'''
array  = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)) :
    for j in range(i,0,-1) :
        if array[j-1] > array[j] :
            array[j], array[j - 1] = array[j - 1], array[j]
        else :
            break
print(array)

'''퀵 정렬 소스코드'''
array  = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end) :
    if start >= end :
        return
    pivot = start
    left = start + 1
    right = end

    #왼 큰 / 오 작 찾기
    while left <= right :
        while left <= end and array[left] <= array[pivot] :
            left += 1
        while right > start and array[right] >= array[pivot] :
            right -= 1
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[right], array[left] = array[left], array[right]

    quick_sort(array,start,right-1)
    quick_sort(array,start,right+1)

quick_sort(array,0,len(array)-1)
print(array)

'''파이썬 장점을 살린 퀵 정렬 소스코드'''
array  = [5,7,9,0,3,1,6,2,4,8]
def quick_sort_py(array) :
    if len(array) <= 1 :
        return
    pivot = array[0]
    tail = array[1:]

    left = [x for x in range(tail) if x <= pivot]
    right = [x for x in range(tail) if x > pivot]

    return quick_sort_py(left) + pivot + quick_sort_py(right)
print(quick_sort_py(array))

'''계수 정렬 소스코드'''
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1)

for i in range(len(array)) :
    count[array[i]] += 1
for i in range(len(array)) :
    for _ in range(count[i]) :
        print(i, end= " ")

'''sorted -> 반환만 정렬
    .sort() -> 해당 개체 정렬'''