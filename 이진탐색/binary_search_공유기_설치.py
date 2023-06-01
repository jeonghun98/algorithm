'''공유기 설치'''
n, c = list(map(int, input().split()))

array = []
for _ in range(n) :
    array.append(int(input()))
array.sort()

#gap의 최소와 최대 -> start, end
start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1,n) :
        if value + mid <= array[i]:
            value = array[i]    # value도 업데이트
            count += 1
    if count >= c:  # count가 크면 gap 키우기 -> start 증가
        start = mid + 1
        result = mid
    else:           # count가 원하는 수보다 작으면 gap 줄이기 -> end 감소
        end = mid - 1

print(result)


