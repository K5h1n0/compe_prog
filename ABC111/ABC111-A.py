n = list(input())
s = ""
for i in range(len(n)):
    if n[i] == "1":
        s += "9"
    elif n[i] == "9":
        s += "1"
    else:
        s += n[i]
print(s)