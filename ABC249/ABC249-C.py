#なんでできたのかあまり分からない。bit全探索+aの問題。
n,k = map(int,input().split())
l = []
for i in range(n):
    l.append(list(input()))

ans = 0
for i in range(2**n):
    l2 = []
    for j in range(n):
        if (i>>j) & 1:
            l2.append(l[j])
    #ここまでbit全探索。これより下は、アルファベットがk文字あるか探索。
    alphabet = [0]*26
    for i in range(len(l2)):
        for j in range(len(l2[i])):
            alphabet[ord(l2[i][j])-97] += 1
        if ans < alphabet.count(k):
            ans = alphabet.count(k)
print(ans)

