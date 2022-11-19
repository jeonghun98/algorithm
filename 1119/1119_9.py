# 창고 다각형

n = int(input())
d = []
y_max = 0; x_max = 0; max_i = 0
for i in range(n) :
    x, y= map(int,input().split())
    d.append((x,y))
    if x_max < x : x_max = x
    if y_max < y :
        y_max = y; max_i = x

d.sort()
array = [0] * (x_max+1)
for x, y in d :
    array[x] = y

result = 0; temp = 0; i = 0
for i in range(max_i + 1) :
    if array[i] > temp :
        temp = array[i]
    result += temp
temp = 0
for i in range(x_max, max_i, -1) :
    if array[i] > temp :
        temp = array[i]
    result += temp
print(result)


