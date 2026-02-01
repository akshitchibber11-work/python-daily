# This logic lets user enter a number,
# then prints the sum and count of numbers added

total = 0
count = 0

x = int(input("Enter a number: "))

for i in range(0, x + 1):
    total += i
    count += 1

print("Total Sum is:", total)
print("Total Count is:", count)
