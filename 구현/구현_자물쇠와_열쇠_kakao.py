# 10 자물쇠와 열쇠

def rotate_a_matrix_by_90_degree(a) :
    n = len(a) #행
    m = len(a[0]) #열
    result = [[0] * n for _ in range(m)]
    for i in range(n) :
        for j in range(m) :
            result[j][n-1-i] = a[i][j]
    return result

def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
            if new_lock[i][j] != 1 :
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)

    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n) :
        for j in range(n) :
            new_lock[n+i][n+j] = lock[i][j]
    for roatation in range(4) :
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n-m+1,n*2) : #시간 줄이기 -> n-m+1 하면 겹치는 부분에서 시작
            for y in range(n-m+1, n*2) :
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True :
                    return True
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]