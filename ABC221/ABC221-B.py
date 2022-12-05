import copy
s = list(input())
t = list(input())
s2 = copy.copy(s)
ans = "No"
if s == t:
    ans = "Yes"
    print(ans)
else:
    for i in range(len(s)-1):
        w = s2[i]
        s2[i] = s2[i+1]
        s2[i+1] = w
        if s2 == t:
            ans = "Yes"    
        s2 = copy.copy(s)
    print(ans)
