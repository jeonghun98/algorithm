# 딱지 놀이
n = int(input())
for _ in range(n) :

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count_a = [0] * 5
    count_b = [0] * 5
    for i in range(1, a[0]+1) :
        count_a[a[i]] += 1
    for i in range(1, b[0] + 1):
        count_b[b[i]] += 1

    if count_a == count_b : print("D")
    else :
        for i in range(4,0,-1) :
            if count_a[i] > count_b[i] :
                print("A")
                break
            elif  count_a[i] < count_b[i]:
                print("B")
                break

