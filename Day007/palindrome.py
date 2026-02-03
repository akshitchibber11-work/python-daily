#This program checks if the number entered is Palindrome or not

num = int(input("Enter number: "))

original = num
rev = 0

while num > 0:        
    digit = num % 10           #gets last digit eg.121-> 1
    rev = rev * 10 + digit     #Multiply by 10 to shift digits to left
    num //= 10                 #remove last digit
 
if rev == original:
    print("Palindrome")
else:
    print("Not palindrome")
