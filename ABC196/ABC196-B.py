x = input()
if "." not in x:
    print(int(x))
else:
    x = list(x)
    l = []
    for i in range(len(x)):
        if x[i] != ".":
            l.append(x[i])
        else:
            break
    print("".join(l))