# 종이 자르기 - 정렬
y,x = map(int, input().split())
x_data = []
y_data = []
for i in range(int(input())) :
    a, b = map(int, input().split())
    if a == 0 : x_data.append(b)
    else : y_data.append(b)

x_data.append(x)
y_data.append(y)
x_data.sort()
y_data.sort()
result = 0

b_x = 0; b_y = 0
for i in x_data :
    for j in y_data :
        w = (i - b_x) * (j - b_y)
        result = max(result, w)
        b_y = j
    b_x = i
    b_y = 0
print(result)

