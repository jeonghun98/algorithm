def solution(today, terms, privacies):
    today_y, today_m, today_d = today.split('.')
    today_s = int(today_y + today_m + today_d)
    answer = []
    term = [0 for _ in range(26)]
    for k in terms :
        t_t, t_m = k.split()
        term[ord(t_t) - ord('A')] = int(t_m)

    for i in range(len(privacies)) :
        day, p_t = privacies[i].split()
        add_m = 0
        if term[ord(p_t) - ord('A')] != 0 :
            add_m = term[ord(p_t) - ord('A')]
        p_y, p_m, p_d = map(int, day.split('.'))
        p_m += add_m
        if(p_m > 12) :
            p_m % 12
            p_y += 1
        p_s = int(str(p_y) +(str(p_m) if p_m > 9 else "0" + str(p_m))
             + (str(p_d) if p_d > 9 else "0" + str(p_d)))
        # print(today_s)
        # print(p_s)
        if(today_s >= p_s) :
            answer.append(i+1)
    return answer

if __name__ == "__main__" :
    print(solution())

    '''
    
"2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
>> 1, 3

"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
>>1, 4, 5
    
    '''