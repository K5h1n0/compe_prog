#文字列やリストの1文字目を抜き出すというやり方をしない。1つ前にずらしていく処理が入るらしく、ものすごく時間がかかる。例えば、s = s[1:]をforループしない。
s = input()
if s == s[::-1]:
    print("Yes")
    exit()
else:
    begin = 0
    end = 0
    s = list(s)
    for i in range(len(s)):
        if s[-1] == "a":
            begin += 1
            s.pop()
        else:
            break
    s.reverse()
    for i in range(len(s)):
        if s[-1] == "a":
            end += 1
            s.pop()
        else:
            break
    if s == s[::-1] and begin >= end:
        print("Yes")
    else:
        print("No")