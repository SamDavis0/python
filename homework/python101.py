# TIP CALCULATOR
# good = 20% 
# fair = 15% 
# bad = 10%

# bill = float(input("What is the total: "))

# service_quality = (input("What kind of tip would you like to leave, good, fair, or bad?: "))

# number_of_people = int(input("How many are dining?"))

# if service_quality == "good":
#     tip = bill * .20
# elif service_quality == "fair":
#     tip = bill * .15
# elif service_quality == "bad":
#     tip = bill * .10
# else:
#     print("Enter the bill please")

# total = bill + tip

# print("Tip: $%.2f" % tip)
# print("Total: $%.2f" % total)
# print(f"Per person: ${total / number_of_people}")



#COIN

# coin = 0

# wants_coin = True

# while wants_coin:
#     answer = input("Do you want another?")
#     if answer.lower() == "yes":
#         coin += 1
#         print(f"You have {coin} coins")
#     elif answer.lower() == "no":
#         print("OKAY BYE")
#         break



#BOX

# width = int(input("Width: "))
# height = int(input("Height: "))

# for x in range(1, width+1):
#     for y in range(1, height+1):
#         if (x == 1 or x == width or y == 1 or y == height):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#TRIANGLE

# height = int(input("Height: "))
# counter = 0
# blanks = height
# stars = 1
# while counter < height:
#     print(" " * blanks+"*" * stars )
#     counter += 1
#     blanks -= 1
#     stars += 2



#MULTIPLICATION TABLE

# for x in range(1, 11):
#     for y in range(1, 11):
#         print(f"{x} x {y} = {x * y}")