# # WHAT IS INPUT AND OUTPUT ?
# # INPUT is the data you give to the program while it's running
# # OUTPUT is the data the program sends back to you 

# # OUTPUT in python 
# # We use print() function to show output

# # Basic example :
# print("Hello, World!")

# # Printing variables
# name = "Mike"
# print("Hello,", name)

# # Printing multiple items
# print("I am", 20, "years old")

# # Formatting output
# age = 20
# print(f"I am {age} years old")  # f-string formatting

# # INPUT in python 
# # We use the input() function 

# # Basic example
# name = input("What is your name? ")
# print("Hello,", name)

# # Converting to integer
# age = int(input("Enter your age: "))
# print("You will be", age + 1, "next year.")

# # Converting to float
# height = float(input("Enter your height in meters: "))
# print("Your height is", height, "meters.")

# # Combining INPUT and OUTPUT
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(f"Hello {name}, you are {age} years old.")

test = "hello world"                                                                                                     
print(test.upper())

test = " python "
print(test.strip(" "))

test = "12345"
print(test.isdigit())

test = "hello world"
print(test.find("world"))

test = "I love Java"
print(test.replace("Java", "Python"))

test = "hello world"
print(test.count("o"))

test = "python is fun"
print(test.title())

test = "apple,banana,cherry"
print(test.split(","))

test = ["I", "love", "Python"]
print(" ".join(test))

test = "PYTHON"
print(test.isupper())

name = input("What is your name: ")
print(name.upper())
print(name.lower())
print(name.title())

name = " ...Mike..."
print(name.strip(" ."))

name = "Mike"
age = 20
print(f"My name is {name} and I am {age} years old")

test = "hello123"
print(test.isdigit())

test = "I LOVE PYTHON"
print(test.lower())