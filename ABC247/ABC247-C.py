#再帰を使う問題。試しにメモ化再帰も使ってみた。メモ化再帰をするのに必要なのは上の3行。
from functools import lru_cache

@lru_cache
def f(k):
    if k == 1:
        return "1"
    else:
        return f(k-1) + " " + str(k) + " " + f(k-1)

n = int(input())
print(f(n))

"""
def kannsuu(n):
    if n == 1:
        return 1
    else:
        return kannsuu(n-1) + n + kannsuu(n-1)

n = int(input())

print(kannsuu(n))
"""