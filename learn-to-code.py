# Strings
first_name = "Chris"
last_name = "Python"
print(first_name + last_name)

# Add a space
print(first_name + " " + last_name)


#.format() ans f strings
first_name = "John"
surname = "Doe"
print("My first name is {}. My family name is {}".format(first_name, surname))

firstname = "Jane"
surname = "Doe"
print(f"My first name is {firstname}. My family name is {surname}")

my_int = 50
sentence = "The total comes to: "
print(sentence + str(my_int))

# Dictionaries
user = {"first_name":"Ada"}
print(user)

user = {"first_name":"Ada"}     # Read
print(user["first_name"])

user["family_name"] = "Byron"   # Update add a key-value, modify by changing value 
print(user)

del user["family_name"]    # Delete key-value pair
print(user)

# Lists
fruit = ["apples", "oranges", "bananas"]
print(fruit[1])
len(fruit)
print(fruit[-1])
print(fruit[-2])

fruit.append("kiwi")
print(fruit)

fruit.insert(2, "passion fruit")
print(fruit)

print(sorted(fruit))

print(fruit)

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

del fruit[1]
print(fruit)

favorite_fruit = fruit.pop()
print(favorite_fruit)

fresh_fruit = fruit.pop(1)
print(fresh_fruit)

fruit.remove('bananas')
print(fruit)

# Determing type
my_variable = "A string"
print(type(my_variable))

my_number = 50
some_string = "The number is "
print(some_string + my_number)