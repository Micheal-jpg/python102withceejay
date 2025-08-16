# STRING METHODS 
# STRING 
# A sequence of characters inside quotes. 
# Can be single quotes(' '), double quotes(" "), or triple quotes(""" """ or  ''' ''')

# STRING METHOD 
# A method  is basically a function that belongs to an object (in this case, a string object). 
# You call it using dot notation

# TYPES OF STRING METHODS
# A. CHANGING CASE
text = "Python is Fun"
print(text.upper())   # 'PYTHON IS FUN'
print(text.lower())   # 'python is fun'
print(text.title())   # 'Python Is Fun'
print(text.capitalize())  # 'Python is fun'
print(text.swapcase())    # 'pYTHON IS fUN'

# B. REMOVING SPACE / CHARACTERS
word = "   hello   "
print(word.strip())   # "hello"  (removes spaces both sides)
print(word.lstrip())  # "hello   " (left side only)
print(word.rstrip())  # "   hello" (right side only)
# you can also strip specific characters
print("...Mike...".strip("."))  # "Mike"

# C. SEARCHING & FINDING
msg = "I love Python"
print(msg.find("love"))   # 2 (position found)
print(msg.find("Java"))   # -1 (not found)
print(msg.index("love"))  # 2 (like find but throws error if not found)
print(msg.count("o"))     # 2 (number of times 'o' appears)

# D. REPLACING
text = "I love Java"
print(text.replace("Java", "Python"))  # 'I love Python'

# E. CHECKING CONTENT
# These return True or False 
word = "Python123"
print(word.isalpha())  # False (contains numbers)
print("Python".isalpha())  # True
print(word.isdigit())  # False
print("12345".isdigit())  # True
print("python".islower()) # True
print("PYTHON".isupper()) # True
print(" ".isspace())      # True

# F. SPLITTING & JOINING
text = "apple,banana,cherry"
print(text.split(","))   # ['apple', 'banana', 'cherry']

words = ["I", "love", "Python"]
print(" ".join(words))   # "I love Python"

# G. FORMATTING STRINGS
name = "Mike"
age = 20
print(f"My name is {name} and I am {age} years old.")  # f-string
print("My name is {} and I am {} years old.".format(name, age))

# Practice on String Methods

# 1. Create a string "hello world" and use a method to convert it to uppercase.
test = "hello world"                                                                                                     
print(test.upper())

# 2. Given " python ", remove the extra spaces at the beginning and end.
test = " python "
print(test.strip(" "))

# 3. Check if the string "12345" contains only digits.
test = "12345"
print(test.isdigit())

# 4. How would you find the position of "world" in "hello world"?
test = "hello world"
print(test.find("world"))

# 5. Replace "Java" with "Python" in the string "I love Java".
test = "I love Java"
print(test.replace("Java", "Python"))

# 6. Count how many times the letter "o" appears in "hello world".
test = "hello world"
print(test.count("o"))

# 7. Turn "python is fun" into "Python Is Fun" using a string method.
test = "python is fun"
print(test.title())

# 8. Split the string "apple,banana,cherry" into a list.
test = "apple,banana,cherry"
print(test.split(","))

# 9. Join the list ["I", "love", "Python"] into a single string with spaces.
test = ["I", "love", "Python"]
print(" ".join(test))

# 10. Write a string method to check if "PYTHON" is in all uppercase.
test = "PYTHON"
print(test.isupper())

# 11. Write a program that asks for a user’s name and prints it in:
# Uppercase
# Lowercase
# Title case
name = input("What is your name: ")
print(name.upper())
print(name.lower())
print(name.title())

# 12. Given the string " ...Mike...", remove the dots and spaces so only "Mike" remains.
name = " ...Mike..."
print(name.strip(" ."))

# 13. Format this data into a sentence: name = "Mike", age = 20 → "My name is Mike and I am 20 years old."
name = "Mike"
age = 20
print(f"My name is {name} and I am {age} years old")

# 14. Check whether the string "hello123" contains only letters.
test = "hello123"
print(test.isdigit())

# 15. Convert "I LOVE PYTHON" into "i love python" using one method.
test = "I LOVE PYTHON"
print(test.lower())