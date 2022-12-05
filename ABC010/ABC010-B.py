n = int(input())
l = list(map(int,input().split()))
cnt = 0
l_maisuu = [0,1,0,1,2,3,0,1,0] #ハードコーディング。スマートでない
for i in range(len(l)):
    cnt += l_maisuu[l[i]-1]
print(cnt)