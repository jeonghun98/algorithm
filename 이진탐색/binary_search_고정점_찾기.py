'''고정점 찾기 - 시간복잡도 O(logN)'''
def find_index(array, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    if mid == array[mid] :
        return mid
    elif mid < array[mid] :
        return find_index(array, start, mid - 1)
    else :
        return find_index(array, mid + 1, end)

n = int(input())
data = list(map(int,input().split()))

result = find_index(data, 0, n-1)
if result == None : print(-1)
else : print(result)