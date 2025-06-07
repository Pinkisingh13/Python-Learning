
# ! 03/06/25
# //?--------------------------------------------------------------------------------------------------------------------------------------------

a = 7
b = 3
print('Comparisons')

# a=7
# b=3
# print('a == b is', a == b)
# print('a != b is', a != b)
# print('a > b is', a > b)
# print('a < b is', a < b)
# print('a >= b is', a >= b)
# print('a <= b is', a <= b)
# print('o in John is ','o' in 'John') #membership
# print('o in John is ','o' not in 'John') #non membership
# print('John is John ','John' is 'John') #identity
# print('John is not John is ','John' is not 'John') # negative identity


# ?---------------------------------------------------------------------------

# ! Identical checking - cheking are a and b are same
# a = [3,7,42]
# b = a
# print(a == b)
# print(a is b) # OUTPUT: true => pointing to the same memory reference # if there memory reference is same. we can check it by is keyword method.

# print(id(a), id(b)) 


#!Identical Checking -  a and b is Not pointing to the same memory adderess. so  (a is b ) will return false
# a = [3,7,42]
# b = [3,7,42]
# print(a == b)
# print(a is b) # OUTPUT: FALSE
# print(id(a), id(b))

# ! Some other Checkings

# print(int(True)) # 1
# print(int(False)) # 0

print(bool('Parrot')) # True
print(bool(' ')) #True
print(bool('')) # False
print(bool(42))  # True
print(bool(0)) # False
print(bool([])) # False
print(bool([1])) # True

#! Python does Bool Conversion Automatically
print( 42 + True) # OUTPUT ==>  42 + 1 = 43
print(42 + False) # OUTPUT => 42 + 0 = 42