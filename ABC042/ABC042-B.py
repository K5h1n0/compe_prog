#変に難しく考えちゃったけど、単にこれで正解になるらしい。
n,l = map(int,input().split())
l_moji = []
for i in range(n):
    l_moji.append(input())
l_moji.sort()
print(*l_moji,sep="")