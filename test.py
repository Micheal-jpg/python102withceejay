# VARIABLES
# name = "Micheal"
# dob = 31/12/2004
gender = "M"
admin = True  
# age = 100
# food = "Rice"
print(gender)

# DATA TYPES
# 1. STRING ('str')
name = "Micheal" #("")
print(name)

# 2. INTEGER ('int')
age = 25 #(Whole numbers)
print(age)

# 3. FLOAT ('float')
price = 10.933 #(decimal numbers)
print(price)

# 4. COMPLEX DATATYPES ('complex')
z = 3 + 5j #(complex)
print(z)

# SEQUENCE TYPES
# 1. LISTS (A mutable collection of data)
colours = ["red", "green", "yellow"]
print(colours)

# 2. TUPLE (An immutable list)
fruits = {"mango", "orange", "banana"}
print(fruits)

# 3. RANGE (represent a sequence of numbers)
range = (1, 11) #(Python is half stop interval so it doesn't print the last value )
print(range)

# MAPPING TYPES
# 1. DICTIONARY (Key and value)
user = {
    "name": "Micheal"
}
print(user)

# 2. BOOLEAN (True or False)
is_admin = True
print(is_admin)

# SET (An unordered collection of unique element)
food = {"Beans", "Rice"}
print(food)

# FROZEN SET (An immutable set)
frozen = frozenset([1, 2, 3])
print(frozen)

# LIST METHODS
# 1. APPEND (add item to end of a list)
people = ["Micheal", "David"]
people.append("Seyi")
print(people)

# 2. CLEAR (clears all the item in a list)
number = [1,2]
number.clear()
print(number)

# 3. COPY (creates a shallow copy of the list allowing separate modification without affecting the original)
subject = ["Maths", "Eng"]
copy_subject = subject.copy()
copy_subject.append("Phy")
print(subject)
print(copy_subject)

# 4. COUNT (counts the occurrences of a specied value in a list)
laptop = ["hp", "dell", "macbook", "hp"]
laps = laptop.count("hp")
print(laps)

# 5. EXTEND (extend allows for adding elements from another iterable to the end of a list)
school = ["College", "Uni"]
school2 = ["High-school"]
school.extend(school2)
# school.extend([school2])  # if you want to put it as a list inside the list
print(school)

# 6. INDEX (index returns the first index of a specified value in a list)
subject = ["Maths", "Eng"]
print(subject.index('Maths'))

# 7. INSERT (insert allows for adding an element at a specified index in the list)
people = ["Micheal", "David"]
people.insert(1, 'Seyi')
print(people)

# 8. REMOVE (it deletes the first occurrence of a specified value in a list)
people = ["Micheal", "David"]
people.remove('David')
print(people)

# 9. POP (it removes and return the last element of the list by default)
people = ["Micheal", "David"]
popped = people.pop()
print(people)
print(popped)

# 10. REVERSE (reverses the order of the list)
people = ["Micheal", "David", "Seyi"]
people.reverse()
print(people)

# 11. SORT (it arranges the elements of the list in ascending order by default)
people = ["Micheal", "David", "Seyi"]
people.sort()
print(people)

# DICTIONARIES WORKING WITH KEY-VALUE PAIRS
students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Eng']}
print(students['name']) # access a specific value in the dictionary 
print(students.get('phone')) # the get method shows us that instead of receiving an error when we try to get a value that is not in the dictionary it tells us it is not part of the dictionary

# We can also update the entire dictionary using the keyword update to add the phone or change any key in the dictionary
students.update({'name': 'Micheal', 'phone': '09187262397'}) 
print(students)

# We can also delete a key from the dictionar using two ways 
del students["courses"]
print(students)  # or by using pop 

# To see how many keys in our dictionary
print(len(students))

# To see all the keys in the dictionary
print(students.keys())

# To see all the values in our dictionary
print(students.values())

# To see both key and values in our dictionary
print(students.items())

# To loop through our dctionary
for key, value in students.items():
    print(key, value)