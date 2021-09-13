#FUNCTIONS HOMEWORK
# 1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.

# It should return the smallest number in the List.

def smallest(list):
    x = 0
    for num in list:
        if num < x:
            x = num
    return x

list1 = [8, -3, 12, 14]

print(smallest(list1))


# 2. Find the largest number
# Write a function largest that accepts a List of numbers as an argument.

# It should return the largest number in the List.

def largest(list):
    x = 0
    for num in list:
        if num > x:
            x = num
    return x

list2 = [14, 0, -5, 20]

print(largest(list2))

# 3. Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.

def shortest(list):
    x = list[0]
    for string in list:
        if len(string) < len(x):
            x = string
    return x
    


list3 = ["hamburger", "egg", "potato", "ketchup"]

print(shortest(list3))

# 4. Find the longest String
# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.

def longest(list):
    x = list[0]
    for string in list:
        if len(string) > len(x):
            x = string
    return x
    
list4 = ["mustard", "relish", "ham", "worchestirshire or however you spell it"]

print(longest(list4))









