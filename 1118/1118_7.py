# 괄호

n = int(input())
for _ in range(n) :
    count = 0
    data = list(input())
    for i in range(len(data)) :
        if data[i] == '(' :
            count += 1
        else :
            count -= 1
            if count < 0 :
                break
    if count == 0 :
        print("YES")
    else :
        print("NO")