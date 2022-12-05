import math
#コンテスト後に書いたもの。円ではWAになってしまう。

print("任意の大きさ(数字)を入力してください")
ookisa = int(input())
for i in range(1,ookisa):
    for j in range(1,ookisa):
        r = i
        c = j
        kyoria = abs((ookisa//2)-r)
        kyorib = abs((ookisa//2)-c)
        hannkei = math.sqrt(kyoria**2 + kyorib**2)
        # print(hannkei)
        if int(hannkei)%2 == 0:
            print(".",end=" ")
        else:
            print("#",end=" ")
    print()