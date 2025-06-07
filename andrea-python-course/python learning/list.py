
# //! 01/06/25
# //?--------------------------------------------------------------------------------------------------------------------------------------------


# //! Example 1: List Basics 1
# friends = ['John','Michael','Terry','Eric','Graham']
# print(friends)
# print(friends[4])
# print(friends[2 : 4])
# print(friends[::-1])
# print(len(friends))
# print(friends.index("Terry"))
# print(friends.count("Graham"))


# //! Example no 2: List Basics 2

friends = ['John','Michael','Terry','Eric','Graham']

# print(friends)

# friends.sort() # Ascending order
# print(friends)

# friends.sort(reverse = True) # Descending order
# print(friends)

# friends.reverse() # To reverse the arrays elements from last index -> first index
# print(friends)

# print(min(friends)) # Eric
# print(max(friends)) # Terry

# print(sum(friends)) # Error: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# //! Example no 3: List Basics


# cars = [911,130,328,535,740,308]
# print(cars)

# print(min(cars))
# print(max(cars))
# print(sum(cars))

# //! Append in the list
# cars = [911,130,328,535,740,308]

# friends.append('FOO')
# print(friends)

# friends.insert( 3,'Boo'),
# print(friends)

# friends[1] = "Jack"
# print(friends)
 
 
# friends.extend(cars)
# print(friends)
 
 
#  //! Remove from list
# print(friends)

# friends.remove('FOO')
# print(friends)


# friends.pop(-1) 
# print(friends)

# friends.clear() #//? list will become empty

# del friends #//? list will be completely deleted

# Delete part of the friends list
# del friends[2]
# print(friends)
 
 
 # //! Copy of the list
# print(friends)

# ! First way
# new_friends = friends[:] #//* this will create new list 
# print(new_friends)

# ! Second way
# new_friends = friends.copy() # * this will create new list also
# print(new_friends)

# ! Third Way
# new_friends = list(friends)
# print(new_friends)

# !  EXERCISE

# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []

# new_day = int(input("How much profit you have: "))

# sales_w2.append(new_day)
# print(sales_w2)


# ! One Way to combine both list
# sales = sales_w1 + sales_w2
# print(sales)

# ! Second way to combine bith list
# sales.extend(sales_w1)
# sales.extend(sales_w2)
# print(sales)


# ! Task 3: 
# sales.sort()
# best_day_profit = sales[-1] * 1.5
# worst_day_profit = sales[0] * 1.5

# print(f'Worst day profit:$ {worst_day_profit}')
# print(f'Best day profit:$ {best_day_profit}')
# print(f'Combined profit:$ {worst_day_profit + best_day_profit}')
  
  
  