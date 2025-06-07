# //! 02/06/25
# //?--------------------------------------------------------------------------------------------------------------------------------------------

#  ! Example 1 :
# msg ='Welcome to Python 101: Split and Join'

# msg2 ='Welcome  to Python   101: Split   and Join'

# csv = 'Eric,John,Michael,Terry,Graham'

# friends_list = ['Eric','John','Michael','Terry','Graham']

# print('Welcome to Python 101: Split and Join')

# ! Split

# * Converting string char to a list
# print(list(msg))


#! Splitting the string into list
# print(msg.split())  # here it will not take mepty space in the list

# print(msg2.split(" ")) # here it will contain space also in the list 

# print(csv.split(',')) # comma seperated list

# ! Converting list into an string
# print(','.join(friends_list))

# print(' '.join(msg.split()))
# print(msg.replace(" ", ''))


# ! Exercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

# ! Task 1 : 
print(csv)

# //! first way using split and join
# friends_list = ','.join(':'.join(csv.split(';')).split(':')).split(',')
# print(friends_list)

# //!  second way using replace
csv = csv.replace(';', ',').replace(':', ',')
print(csv)

friends_list = csv.split(",")
print(friends_list)

