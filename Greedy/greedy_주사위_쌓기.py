# 주사위 쌓기 - 완전탐색

n = int(input())
data = []
for _ in range(n) :
    data.append(list(map(int, input().split())))

dice_dic = {0:5,1:3,2:4,3:1,4:2,5:0}
result = 0

for i in range(6) :
    one_dice = [1,2,3,4,5,6]

    bottom = data[0][i]
    top = data[0][dice_dic[i]]

    one_dice.remove(bottom)
    one_dice.remove(top)

    max_n = [max(one_dice)]
    for j in range(1,n) :
        dice = [1, 2, 3, 4, 5, 6]
        t_index = data[j].index(top)

        bottom = data[j][t_index]
        top = data[j][dice_dic[t_index]]

        dice.remove(bottom)
        dice.remove(top)

        max_n.append(max(dice))
    result = max(result, sum(max_n))
print(result)


