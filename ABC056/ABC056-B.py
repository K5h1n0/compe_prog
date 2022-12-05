#問題文がよく分からない
#解説AC

w,a,b = map(int,input().split())
if abs(a-b) <= w:
    print(0)
else:
    print(abs(a-b)-w)


"""
#他の人の解答
#swapのやり方とか、if文を一文で書けるようになったほうが良い。
w, a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(b-(a+w) if b > a+w else 0)
"""