# 07 럭키 스트레이트
n = list(map(int, input()))
#print(n)
leng = len(n) // 2

if sum(n[0:leng]) == sum(n[leng:]) :
    print("LUCKY")
else :
    print("READY")
