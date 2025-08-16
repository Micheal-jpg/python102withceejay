# OPERATORS

# ARITHMETRIC OPERATORS
a = 15
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b) # Exponentiation

# COMPARISON OPERATORS
x = 10
y = 20
print(x == y) # equality operator
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

# LOGICAL OPERATORS
x = 7
print( x > 5 and x < 15)
print( x < 5 or x < 15 )
print( not(x == 7)) # reverse of the answer (not)

# IDENTITY OPERATORS
a = [1, 2, 3]
a = b
c = [1, 2, 3]
print(a is b) # True, both refer to the same object
print(a is not c) # True , both are different objects
print(a is c) # False, a and c are different objects

# MEMEBERSHIP OPERATORS
my_list = [1, 2, 3, 4]
print(2 in my_list) # True
print(6 not in my_list)
print(20 in my_list)

# Practice
# 1. Use the modulo operator (%) to check if a number is even
x = 10
print(x % 2 == 0)

# 2. Compare two numbers using relational operators and print which one is greater,
w = 12
z = 15
print(w > z)
print(w < z)
print("Greater", z)

# 3. Check if the letter "a" exists in the word "banana" using the membership operator
x = "banana"
print("a" in x) 

# 4. Print "Access denied" if the user is NOT an admin using the NOT operator
user = 'admin'
print(not user == 'guest' and 'Access denied')

# 5. Use the identity operator to check if two lists are the same object in a memory
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x is y)

# 6. You have 29 apples and each box hold 4 apples. use the floor division to find out how many full boxes you can fill
apples = 29
box = 4
floor_division = apples // box
print(floor_division)

# 7. Count how many numbers in a list are greater than 50
numbers = [10, 55, 60, 40, 75, 50, 90]
count = sum(num > 50 for num in numbers )
print(count)

# 8. Check if a keyword is in a sentence and the sentence starts with that keyword using membership and logical operators
sentence = "Python is awesome"
keyword = "Python"
print(keyword in sentence and sentence.startswith(keyword) and "Keyword found and sentence starts with it")

# 9. Check if a number is between 10 and 20 using logical AND
num = 15
if num >= 10 and num <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is NOT between 10 and 20.")