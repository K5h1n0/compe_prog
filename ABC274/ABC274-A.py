from decimal import ROUND_HALF_UP, Decimal
a,b = map(int,input().split())
print(Decimal(str(b/a)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))