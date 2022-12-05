n = int(input())
m = n//60
s = n - m*60
h = m//60
m -= h*60
ans = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
print(ans)