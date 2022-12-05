#正攻法が分からない
n = int(input())
l = []
for i in range(1,n+1):
    l.append(10000*i/n)
print(int(sum(l)))