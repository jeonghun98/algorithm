'''못생긴 수'''
n = int(input())

data = [0]*n
data[0] = 1

n2, n3, n5 = 2, 3, 5
n2_i = n3_i = n5_i = 1

for i in range(1, n) :
    data[i] = min(n2, n3, n5)
    if data[i] == n2 :
        n2 = 2 * data[n2_i]
        n2_i += 1
    if data[i] == n3 :
        n3 = 3 * data[n3_i]
        n3_i += 1
    if data[i] == n5 :
        n5 = 5 * data[n5_i]
        n5_i += 1

print(data)
print(data[n-1])

