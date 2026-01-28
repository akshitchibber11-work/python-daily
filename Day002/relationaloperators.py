#AND, OR, NOT Questions
#AND: Checks both and if both are true, returns true
x = 20
y = 40
z = x < y and y > x
print(z)

#OR: Checks if any one of the conditions is true and returns true else will return false
x = 20
y = 40
z= x > y or y < x
print(z)

#NOT: Checks if any one of the conditions is true and returns its opposite(T->F, F->T)
x = 20
y = 40
z = not x > y
print(z)
