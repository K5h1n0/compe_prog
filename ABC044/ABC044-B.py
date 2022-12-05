w = list(input())
if len(w)%2 == 1:
    ans = "No"
else:
    ans = "Yes"
    w.sort()
    for i in range(len(w)):
        if i % 2 == 0:
            tmp = w[i]
        else:
            if tmp == w[i]:
                pass
            else:
                ans = "No"
                break
print(ans)