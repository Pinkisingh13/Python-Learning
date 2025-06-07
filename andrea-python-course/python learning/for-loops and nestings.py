
# ! 05/06/25
# //?--------------------------------------------------------------------------------------------------------------------------------------------

# for letter in 'Norwegian blue':
#     print(letter)

# print("For Loop done!")


# ! RANGE
# for letter in  range(1,15,2):
#     print(letter)

# print("For Loop done!")

# ! Loop in list

# for name in ['John','Terry','Eric','Michael','Gimmy']:
#     print(name)

# print("For Loop done!")

#! length of a list
# friends = ['John','Terry','Eric','Michael','George']
# for index in range(len(friends)):
#     print(friends[index])

# print("For Loop done!")

# ! For loop Exercise


# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']
# msg = 'You are invited to the party on saturday.'
# names.extend(names1)

# for index in range(2):
#     names.append(input('Enter a new name: '))


# for name in names:
#     print(f"{name.title()}! {msg} ")
     
     
     
     
# !    Enumerate this! 

print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

for num, friend in enumerate(friends,51):
    print(num, friend)
for friend in enumerate(friends,51):
    print(friend)
for friend in enumerate(enumerate(friends,51),-100):
    print(friend)   
for num, letter in enumerate('python',start = 5):
    print(num, letter)
print(type(enumerate(friends)))
print(list(enumerate(friends)))