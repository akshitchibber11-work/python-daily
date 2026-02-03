#This progrsm checks if the number is prime or not

num = int(input("Enter a number:"))

#Logic: A prime number is only divisible by itself, so if it's divisible by other values it means its not prime.
for i in range(2,num):
    if num % i == 0:
        print("Number is not prime")
        break

else:
    print("Num is Prime") 