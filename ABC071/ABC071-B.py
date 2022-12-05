s = list(set(list(map(ord,list(input())))))
alphabet = list(range(ord("a"),ord("z")+1))
s.sort()
ans = -1
for i in range(len(alphabet)):
    if alphabet[i] in s:
        ans = -1
        pass
    else:
        ans = alphabet[i]
        break
if ans == -1:
    print("None")
else:
    print(chr(ans))