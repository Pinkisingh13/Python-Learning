# //! 01/06/25
# //?---------------------------------------------------------------------------------------------------------------------------------------------------------

# //! Working With User Inputs


# //! Example no 1: 
# name = input("What is your name? :")
# age = input("what is your age:")

# print(f'Hello, {name.title()}! you are {age} years old! Great.')


# //? --------------------------------------------------------------------------------

# //! Example no 2: 
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# print(f"Add : {num1 + num2}")
# print(f"Substraction : {num1 - num2}")
# print(f"Multiplication : {num1 * num2}")
# print(f"division : {num1 / num2}")
# print(f"Modulus : {num1 % num2}")


# //? --------------------------------------------------------------------------------

# //! Exercise 1

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# //! Solution: 
# name = input("enter your first name: ")
# distance_in_km = float(input("Enter the distance (in km): "))

# print(f"Hello, {name.title()}! km is {(distance_in_km)}, and miles is  { round(distance_in_km / float(1.609), 5)} ")
 