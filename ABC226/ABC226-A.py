from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
n = str(input())
n = Decimal(n).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(n)

#文字列型で受け取った後に、"."でスプリットしている人もいる。
