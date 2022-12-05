print("大きさ(数値)を入力してください")
ookisa = int(input())
for i in range(1,ookisa):
    for j in range(1,ookisa):
        kyoria = abs((ookisa//2)-i)
        kyorib = abs((ookisa//2)-j)
        if max(kyoria,kyorib)%2 == 0:
            print("." , end = " ")
        else:
            print("#",end = " ")
    print()