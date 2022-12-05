s = input()
t = input()
if len(s) < len(t):
    print("No")
elif t in s:
    print("Yes")
else:
    print("No")