
# ! 02/06/25
# //?--------------------------------------------------------------------------------------------------------------------------------------------

#! Sets: sets use curly brackets and the main difference between list and set is that a set is unordered and it also removes duplicates that are inside it. Set also a lot faster at finding members (searching ) inside the set than a list is.
 
# friends = ['John','Michael','Terry','Eric','Graham']

# friends_tuple = ('John','Michael','Terry','Eric','Graham')

# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}

# print(friends)
# print(friends_tuple)
# print(friends_set)


#! Intersection in  set 
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# print(friends_set.intersection(my_friends_set))

#! Difference in  set 
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# print(friends_set.difference(my_friends_set))

#! Union in  set 
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# print(friends_set.union(my_friends_set))

#! Empty state

#! empty Lists
# empty_list = []
# empyt_list = list()

#! empty Tuple
# empty_tuple = ()
# empty_tuple = tuple()

#! empty Set: should always command with set{}
# empty_set = {} # this is wrong, this is a dictionary
# empty_set = set()



# ? --------------------------------------------------------------------------------------------

# ! Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']


# ! Task 1: 
# print('Eric' in friends and 'John' in friends)

# ! Task 2: 
# print(friends.union(my_friends))

# ! Task 3:
# print(friends.intersection(my_friends))

#! Task 4: 
# print(friends.difference(my_friends))

# print(friends-my_friends) # it can also be  used to get difference element which are not in the other set.

#! Task 5:
print(friends ^ my_friends)

#! Task 6: 
print(set(cars))
print(list(set(cars))) # first convert to set and remove duliates then convert back to list