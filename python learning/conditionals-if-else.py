
# ! 03/06/25
# //?------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#! Conditionals: IF statements
# print("Conditionals: IF statements")

# is_raining = False

# print("Good Morning")
# if is_raining:
#     print("Bring umbrella!")
# else:
#     print("Don't bring umbrella!")


#? ------------------------------------------------------------------------------------------

#! OR Condition checking
# is_raining = True
# is_cold = True
# print("Good Morning!")
# if is_raining or is_cold:
#     print("Bring umbrella or jacket or both!")
# else:
#     print("Umbrella optional!")

#? ------------------------------------------------------------------------------------------

#! AND Condition checking
# is_raining = True
# is_cold = False
# print("Good Morning!")
# if is_raining and is_cold: 
#     print("Bring umbrella or jacket or both!")
# else:
#     print("Umbrella optional!")
    
#? ------------------------------------------------------------------------------------------

# is_raining = True
# is_cold = False
# print("Good Morning!")

# if is_raining and is_cold: 
#     print("Bring umbrella and jacket!")
# elif is_raining and not(is_cold):
#     print("Bring umbrella!")
# elif not(is_raining) and is_cold:
#     print("Bring jacket!")
# else:
#     print("Shirt is fine!")


#  ! Example 

# amount = 51
# if amount <= 50:
#     print("Purchase approved")
# else:
#     print("Please enter your PIN")


#! EXERCISE -  Build a Calculator

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# first_number = int(input("Enter First Number: "))
# second_number = int(input("Enter Second Number: "))
# operator = input("Enter Operator You want to perform: ") 

# if operator == '+' :
#     print(first_number + second_number)
# elif operator == '*' :
#     print(first_number * second_number)
# elif operator == '-':
#     print(first_number - second_number)
# elif operator == '/':
#     print(first_number / second_number)
# else:
#     print("Input error!")

# ! Second EXERCISE 
def num_days(month):
    if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    else :
        print('number of days in',month,'is',30)

num_days('oct')
