# 1
#Given two lists of numbers of the same length, create a new list by multiplying the
# pairs of numbers in corresponding positions in the two lists. Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# list3 = []

# for x in range(3):
#     list3.append(list1[x] * list2[x])
# print(list3)

# 2
#Given two two-dimensional lists of numbers of the size
#  2x2 two dimensional list is represented as an list of lists
# Calculate the result of adding the two matrices. The number in each position in 
# the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add

# arr1[0][0] * arr2[0] = arr3[0][0]

# example = [ [2, -2],
#             [5, 3] ]

# list1 = [ [1, 3,],
#             [2, 4,] ]
# list2 = [ [5, 2,],
#             [1, 0] ]
# list3 = []

# for x in range(len(list1)):                       #gathers just the length, not the variable inside a dummy variable
#     answer = []                                   #empty list placement to append to later
#     for y in range(len(list1)):                   #nested loop
#         answer.append(list1[x][y] + list2[x][y])  #adding both lists and appending to our placement

#     print(answer)


#3 
# Use your solution in Matrix Addition, and extend it to work for a pair
#  of matrices of any size, as long as they have the same size.

# list1 = [[1,5,4],[2,3,6],[4,8,9]]
# list2 = [[2,9,3],[4,8,1],[5,7,6]]

# final = []


# for i in range(len(list1)):             #dummy variable just for length (could be either list)
#     temp = []
#     for j in range(len(list1)):
#         element = list1[i][j] + list2[i][j]
#         temp.append(element)
#     final.append(temp)

# print(final)








#4
#Given a list of numbers or strings, create a new
#  list containing the same elements as the first list,
#  except with any duplicate values removed. Print the list.

# list1 = [1, 5, 3, 4, 7]
# list2 = [1, 5, 3, 4, 8]
# list3 = []

# for x in list1:
#     if x not in list2:
#         list3.append(x)
# print(list3)




#5 
# Given a paragraph of text as a String, print the paragraph in leetspeak.
# To translate a String to leetspeak, you need to replace make the following
#  character replacements (treat all input characters as uppercase):

# Example: If your program is given the String "I am a leet programmer", it
#  should print "1 4m 4 l337 pr0gr4mm3r" as the leetspeak translation

# A = 4
# E = 3
# G = 6
# I = 1
# O = 0
# S = 5
# T = 7




#6
# Given a word as a string, print the result of extending any
#  long vowels to the length of 5.
#  Example:
# Good => Goooood 
# Cheese => Cheeeeese 
# Man => Man 
# Spoon => Spooooon 


