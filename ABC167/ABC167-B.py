a,b,c,k = map(int,input().split())
if a > k:
    ans = k
else:
    ans = a
if a + b < k:
    ans -= k-(a+b)
print(ans)