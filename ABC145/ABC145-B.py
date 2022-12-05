n = int(input())
s = list(input())
if n%2 == 1:
    print("No")
else:
    ans = "Yes"
    length = len(s)//2
    for i in range(length):
        if s[i] != s[i+length]:
            ans = "No"
            break
    print(ans)