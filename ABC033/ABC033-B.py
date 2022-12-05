n = int(input())
l_name = []
l_pop = []
for i in range(n):
    name,p = input().split()
    l_name.append(name)
    l_pop.append(int(p))
ans = "atcoder"
for i in range(n):
    if sum(l_pop)//2 < l_pop[i]:
        ans = l_name[i]
print(ans)