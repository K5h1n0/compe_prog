from collections import defaultdict,deque

n = int(input())
l = defaultdict(list) #defaultdictのここは、intもあれば、このようにlistでも良い。
hantei = defaultdict(int)
for _ in range(n) :
	a, b = map(int, input().split())
	hantei[a] = False
	hantei[b] = False
	l[a].append(b)
	l[b].append(a)
#print(l)
#print(hantei)
q = deque()
q.append(1)
hantei[1] = True
ans = 1
while q:
	now = q.popleft()
	if ans < now:
		ans = now
	for i in l[now]:
		if hantei[i] == False:
			q.append(i)
			hantei[i] = True
			#print(i)
print(ans)