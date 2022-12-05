n = int(input())
l = list(map(int,input().split()))
l.sort
l3 = dict(zip(list(range(1,n+1)),[0]*n))
for i in l:
    l3[i] += 1
for i in l3.values(): #辞書型の値のみ出力したい時はこれ！！
    print(i)