#嘘解法。最大公約数や、最小公倍数くらいは、本当は自分で求められるようになっておかなきゃいけないと思う。
import math

a,b = map(int,input().split())
print(a*b//math.gcd(a,b))