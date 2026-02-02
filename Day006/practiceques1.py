# 1.	Check whether the given number is divisible by 3 and 5 both.

x = int(input("Enter a number: "))

if x % 3 == 0 and x % 5 == 0:
    print("Divisible by both 3 and 5")

elif x % 3 == 0 or x % 5 == 0:
    print("Divisible by only one of them")

else:
    print("Not divisible by 3 or 5")

