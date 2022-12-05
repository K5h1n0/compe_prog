n = int(input())
if n%10 == 3:
    print("bon")
elif n%10 == 2 or n%10 == 4 or  n%10 == 5 or  n%10 == 7 or  n%10 == 9:
    print("hon")
else:
    print("pon")