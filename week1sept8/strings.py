# STRINGS
# "Sam"
# 'Davis'
# # backslash for same-use quotes
# 'I\'m a new developer'
#  multi-line string
# """I'm a long string
# that continues down to the second line"""
# '''So am
# I.'''

# print('Hello' + 'world') Helloworld
# print("3" + "5") 35
# print(3 + 5) 8
# print(3.14 * 2) 6.28

# True # 1
# False # 0

# print(True + True) = 2

# ESCAPE CHARACTERS
# \b backspace
# \t tab  (indention)
# \v vertical tab (an enter typically)
# \n new line (2 carriage returns(2 enters?))

#MATH
# +	Addition
# -	Subtraction
# *	Multiplication
# /	Division
# Multiplication and division have a higher order than addition and subtraction.
# Use parentheses to control the order of operations
# ((5 + 30) * 20) / 10 
# 70.0

# 5    //    2       2      #    division    w/o    decimal    
# 5    %    2       1       #    modulus/remainder    
# 5    **    3       125    #    exponentiation

#VARIABLES
# first_name = "Sam"
# last_name = "Davis"

# print(first_name, last_name)  #Sam Davis
# print(first_name + last_name) #SamDavis
# print(first_name + "   " last_name) #Sam   Davis

# first_name = "Matt"
# last_name = "Fisher"
# # {} = placeholders
# sentence = "Hello {1} {0}, how are you doing today?".format(first_name, last_name)
# sentence2 = "Hello {last} {first}, how are you doing today?".format(first=first_name, last=last_name)
# sentence3 = "Hello {} {}, how are you doing today?".format(first_name, last_name)

# print(sentence, sentence2, sentence3)
# # Hello Matt Fisher, How are you doing today?

# first_name = "joe"
# last_name = "smith"

# sentence = f'Hello {first_name} {last_name} how are you doing today?'
# print(sentence)

# # FUNCTIONS
# print()
# input()   name = input("What is your name?")
#           # print(f'Your name is {name}') 
# int()
# type()    print( type(99.9) )  # float
# isinstance()   print( isinstance(99, in) )  # True
# Math functions


#BOOLEANS
# and = false  unless true and true
# or = true    unless false or false

# 1  true  
# 2  false
# 3  false
# 4  true
# 5  true
# 6  true
# 7  false
# 8  true
# 9  false
# 10 false

# 1  true
# 2  false
# 3  true
# 4  false
# 5  false
# 6  false
# 7  true
# 8  true
# 9  false
# 10 false

# print('hello world')

# print('digital crafts')
# age = 19
# name = "emily"

# if age == 25:
#     print(1)
#     print(2)
#     print(3)
#     if name == "emily":
#         print('emily is here')
# print('outside of my if statement')

# if(age >= 21):
#     print("you can drink")
# elif age < 18:
#     print("go away")
# else:
#     print("almost yo")


# letter = input("Type a vowel: ")

# if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
#     print("Vowel")
# else:
#     print("Not a Vowel")

# counter = 0

# while counter <= 10:  
#     print('Christine')  
#     counter = counter + 1  # counter = 1 + 1 = 11


while True:
    answer = input("Say when: ")

    if answer.lower() == "when":
        break
print("outside of of while loop")

# num = (input("Enter a number or type stop:  ")

# while num != "stop":
#     if int(num) % 2 == 0:
#         print("This is even")
#     elif int(num) % 2 != 0:
#         print("This is odd")
#     else:
#         print("This is odd")


