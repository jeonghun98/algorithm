# -*- coding: utf-8 -*-
'''위에서 아래로'''
# n = int(input())
# data = []
# for i in range(n) :
#     data.append(int(input()))
#
# data = sorted(data, reverse=True)
# for i in data :
#     print(i, end = " ")

'''성적이 낮은 순서로 학생 출력하기'''
# n = int(input())
#
# data = []
# for i in range(n) :
#     input_data = input().split()
#     data.append((input_data[0], int(input_data[1])))
#
# data = sorted(data, key = lambda x : x[1])
# for student in data :
#     print(student[0], end= " ")

'''두 배열의 원소 교체'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

for i in range(k) :
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else :
        break
print(sum(a))