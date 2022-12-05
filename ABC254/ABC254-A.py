n = int(input())
while n > 99:
    n = n - 100
n = str(n)
print(n.zfill(2))



"""
n = int(input())

# zfillの中身のイメージ
n = str(n)
n = list(n)
n = n[1:]
print(n)
"""