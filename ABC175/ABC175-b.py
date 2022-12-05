#ファイル名を間違えて小文字で作成してしまった。
n = int(input())
l = list(map(int,input().split()))
cnt = 0
if n >= 3:
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    if (l[i]>l[j] and l[i]>l[k])and l[i] < l[j]+l[k]:
                        cnt += 1
                    elif (l[j]>l[i] and l[j]>l[k])and l[j] < l[i]+l[k]:
                        cnt += 1
                    elif (l[k]>l[i] and l[k]>l[j])and l[k] < l[j]+l[i]:
                        cnt += 1
print(cnt)