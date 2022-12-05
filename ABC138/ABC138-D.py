#解説AC　#幅優先
from collections import defaultdict, deque

n,q = map(int,input().split())
connect = [] #二次元配列の初期化
for i in range(n+1):
    connect.append([])
for i in range(n-1): #入力受け取り。
    a,b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)

counter = [0]*(n+1) #それぞれの節に加算していくために用意した配列
for i in range(q): #最終的にこのcounterが答えになる。
    p,x = map(int,input().split())
    counter[p] += x #入力時に、一つの節に複数回、値が提示されることがあるので、この書き方になっている。
#print(counter)

queue = deque() #queueの準備。dequeを使うと、配列の左端を取得しても、リストほど時間がかからない。
queue.append(1) #1を入れて、
visited = [False]*(n+1)
visited[1] = True #1を入れたので、訪問済みの所はTrueにする。

#print(connect)
while queue: #queueに何か値が入っている間はループ。

    now = queue.popleft() #queueの左端をpop。
    now_number = counter[now] #足すべき値をcounter配列から取得。

    for to in connect[now]: #こういう書き方もあるのか。
        #print("to",to)
        #print(counter)
        if visited[to] == True:
            pass #訪問済みなら何もしない。
        elif visited[to] == False: #まだ訪問していなければ、
            counter[to] += now_number #counterの配列のそれぞれに、蓄積されていくのか

            visited[to] = True
            #print("toを格納しました",to)
            queue.append(to)

print(*counter[1:])