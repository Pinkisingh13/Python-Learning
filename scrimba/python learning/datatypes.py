
# //! 01/06/25
# //?---------------------------------------------------------------------------------------------------------------------------------------------------------
 
#  //! Data Types [int, str, float, boolean]

failed_subject = 2.45
name = "4.5"
name = 3
is_here = False

a='it\'s'

print(type(failed_subject))
print(name)
print(a)
print(is_here)

# //?--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# //! TYPE CASTING
# Python's int() function can only convert strings that represent whole numbers (like "3"), not decimal numbers.
# Trying to convert "3.4" will raise a ValueError: ValueError: invalid literal for int() with base 10: '3.4'

# //! How to fix:
# If you want to convert "3.4" to an integer, first convert it to a float, then to an int:
# c1 = int(float("3.4"))  # c1 will be 3


# //! Note: 
# Only strings that look like numbers can be converted to numbers.
# Converting a float to int will always truncate (not round) the decimal part.

a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
c1 = int("3.4")   # c1 will be...
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,d,e,f,g,h,i,j])