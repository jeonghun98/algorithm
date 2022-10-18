'''금광'''
def find(array, n, m) :

    # d = [[0] * m for _ in range(n)]
    # for i in range(n) :
    #     d[i][0] = array[i][0]

    for j in range(1,m) :
        for i in range(n) :
            up = 0; left = array[i][j-1]; down = 0
            if i - 1 >= 0 :
                up = array[i-1][j-1]
            if i + 1 < n :
                down = array[i+1][j-1]
            array[i][j] = max(up,left,down) + array[i][j]

    result = 0
    for i in range(n) :
        result = max(result, array[i][m-1])
    print(result)


t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    data = []
    for i in range(n) :
        data.append(temp[i*m:i*m+m])

    find(data, n, m)