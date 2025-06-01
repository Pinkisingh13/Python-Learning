# //! 01/06/25
# //?---------------------------------------------------------------------------------------------------------------------------------------------------------

# //* Strings are immutable
# msg='welcome to Python 101: Strings'
# print(msg)
 
# //! print message multiple times
# print(msg*2)
# print(msg + msg)
# print(msg,msg)

# //?-------------------------------------------------------------------------------------------------------

# //! Change the case of the string
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title()) # //* it actually fails sometimes. for instance, when we have an apostrophe in string. 

# //* Lets take and example

# print("hey, It\'s python course".title()) # //* Output : Hey, It'S Python Course

# //?-------------------------------------------------------------------------------------------------------

# //! Other methods 
# print(len(msg)) # Output: 30 

# //* count() method count how many times a particular character comes in an string
# print(msg.count("o")) # count method is case sensititve

# //?-------------------------------------------------------------------------------------------------------
# //! Slicing String: Get in part of the strings. the counting start from 0 
# //* can use negative indexes also to get the string from back side 

# //* the colon will tell python to grab everything after the given value
# print(msg[-2], msg[3: 6])
# print(msg[:7]) # Output: welcome becuse it take from staring to the 6 index. end index is exclusive.

# //?-------------------------------------------------------------------------------------------------------

# //! Exercise: Python 101: tring Exercise 1

# //! Task 1: Define a new string 
# msg='1 Welcome Ring To Tyler'
# print(msg)

# //!  Task 2: Every first letter in a word should capital
# print(msg.title())

# //! Task 3: print the string backward
# //* The syntax is [start:stop:step].
# Leaving start and stop empty means it takes the whole string.
# The -1 as step means it moves from the end to the start, effectively reversing the string.
# So, msg[::-1] returns a new string with all characters in reverse order.

# length = len(msg)
# print(length)
# print(msg[:: -1])



# //?---------------------------------------------------------------------------------------------------------------------------------

# //! Multiline String
msg='Welcome to Python 101: Strings'
print(msg)

# msg="""Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring!"""
# print(msg)

# //?--------------------------------------------------------------------------------------------------------------------------------

#  //! Find And Replace

# print(msg.find("Python"))
# print(msg.replace("Python","String"))

# //?--------------------------------------------------------------------------------------------------------------------------------


# //! Membership
print('Python' in msg) # True
print('Python' not in msg) # False

# //?------------------------------------------------------------------------------------------------

# //! String Formatting


# //* Concatenate the string
name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'

print(msg)

# //* Format 
msg = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
