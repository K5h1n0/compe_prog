#BFS 幅優先探索
#queue キュー
"""
# 必要なライブラリのインポート
import queue

# FIFOキューの作成
q = queue.Queue()

# キューにデータを挿入する。挿入するデータは「0, 1, 2, 3, 4」
for i in range(5):
    q.put(i)

# キューからデータがなくなるまで取り出しを行う
while not q.empty():
    print(q.get())
"""

import queue
# import time

r,c = map(int,input().split())
starty,startx = map(int,input().split())
goaly,goalx = map(int,input().split())
l = []
for i in range(r):
    l.append(input())
l1 = []
for i in range(r):
    l1.append([0]*c)

#上、右、下、左
x = [0,1,0,-1]
y = [-1,0,1,0]
flg = 0
q = queue.Queue() #queueの使い方はこれ。リストなどのように、構造の一種？っぽい。
starty -= 1
startx -= 1
goaly -= 1
goalx -= 1
q.put([starty,startx,0]) #queueにはputで入れる。
cnt = 0
while flg == 0:
    tmpl = q.get() #queueからは、getで出す。
    nowy = tmpl[0]
    nowx = tmpl[1]
    cnt = tmpl[2] + 1
    if l1[nowy][nowx] == 1:
        continue
    else:
        l1[nowy][nowx] = 1
    #print("今いる場所",nowy,nowx)
    for i in range(4):
        # print("i=",i," ",nowy + y[i],nowx+x[i],cnt) #これで、上から右回りになる。（上、右、下、左）
        if nowy + y[i] == goaly and nowx + x[i] == goalx:
            # print("到達しました")
            ans = cnt
            flg = 1
            break
        elif l[nowy + y[i]][nowx + x[i]] == "." and l1[nowy + y[i]][nowx + x[i]] == 0: #操作した先が"."ならば進める。
            # print(nowy + y[i],nowx+x[i],"格納しました")
            q.put([nowy + y[i],nowx + x[i],cnt])
print(ans)