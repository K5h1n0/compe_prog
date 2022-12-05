s = input()
o = ""
e = ""
for i in range(len(s)):
    if i % 2 == 0:
        e += s[i]
    else:
        o += s[i]
if e.islower():
    if o == "" or o.isupper():
        print("Yes")
    else:
        print("No")
else:
    print("No")