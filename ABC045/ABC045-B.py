sa = list(input()[::-1]) #popができるように文字列反転。s[::-1]で文字列を反転させることができる
sb = list(input()[::-1])
sc = list(input()[::-1])
next = sa.pop()
while True:
    if next == "a":
        if len(sa) == 0:
            ans = "A"
            break
        else:
            next = sa.pop()
    elif next == "b":
        if len(sb) == 0:
            ans = "B"
            break
        else:
            next = sb.pop()
    elif next == "c":
        if len(sc) == 0:
            ans = "C"
            break
        else:
            next = sc.pop()
print(ans)