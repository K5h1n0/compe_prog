l,r = map(int, input().split())
s = input()
s2 = s[l-1:r]
s2 = list(s2)
s2.reverse()
s2 = "".join(s2)
s3 = s[:l-1] + s2 +s[r:]
print(s3)