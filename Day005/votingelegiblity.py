#This logics let's user input their age and checks if they're eligible to vote or not

x = int(input("Enter your age:"))

if x >= 18:
    print("Eligible for voting")

elif x < 18:
    print("Not Eligible for voting")

else:
    print("Input number!")