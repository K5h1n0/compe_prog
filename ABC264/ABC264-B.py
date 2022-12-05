#ハードコーディング。スマートでない
r,c = map(int,input().split())
l = [
    "xxxxxxxxxxxxxxx",
    "xooooooooooooox",
    "xoxxxxxxxxxxxox",
    "xoxoooooooooxox",
    "xoxoxxxxxxxoxox",
    "xoxoxoooooxoxox",
    "xoxoxoxxxoxoxox",
    "xoxoxoxoxoxoxox",
    "xoxoxoxxxoxoxox",
    "xoxoxoooooxoxox",
    "xoxoooooooooxox",
    "xoxxxxxxxxxxxox",
    "xoxxxxxxxxxxxox",
    "xooooooooooooox",
    "xxxxxxxxxxxxxxx",
]
s = list(l[r-1])
s = s[c-1]
if s == "x":
    print("black")
else:
    print("white")