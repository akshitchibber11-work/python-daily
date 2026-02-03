#This prgoram checks if the entered number is armstrong or not.

num = int(input("Enter number: "))

original = num
power = len(str(num))   # number of digits
total = 0

while num > 0:
    digit = num % 10
    total += digit ** power
    num //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not Armstrong")
