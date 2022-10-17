''' 이진 탐색 소스코드'''
'''재귀 함수로 구현한 이진 탐색 소스 코드'''

def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    if target == array[mid] :
        return mid
    elif target < array[mid] :
        return binary_search(array, target, start, mid-1)
    else :
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None :
    print("존재하지 않습니다.")
else :
    print(result + 1)

'''반복문으로 구현한 이진 탐색 소스코드'''

def binary_search2(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if target == array[mid] :
            return mid
        elif target < array[mid] :
            end = mid - 1
        else :
            start = mid + 1
    return None