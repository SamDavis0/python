#TO DO LIST
#In this assignment you are going to create a TODO app. When the app starts it should present user with the following menu:


# Want input(response to question)
# if 1: What priority high, medium or low : 
#   dictionary["new"]: value
# if 2 print (dictionary.items())
# if 3 del dictionary[item]
# if q press q to break while loop



todos = {
    "High"   : ["Mow", "Dishes", "Laundry"], 
    "Medium" : ["Shop", "Run", "Clean"],
    "Low"    :  ["Pay bills", "Vacuum", "Fold" ]
    }


while True:
    question = input("Press 1 to add task \n" "Press 2 to delete task\n" "Press 3 to view all tasks \n" "Press q to quit \n")
    if question == "1":
        
        priority = input("Set priority: High, Medium, or Low\n")
        if priority.capitalize() == "High":
            task = input("Write task: ")
            todos["High"].append(task)
            print(todos.items())
            
        if priority.capitalize() == "Medium":
            task = input("Write task: ")
            todos["Medium"].append(task)
            print(todos.items())
            
        if priority.capitalize() == "Low":
            task = input("Write task: ")
            todos["Low"].append(task)
            print(todos.items())
            
    if question == "2":
        priority = input("In what priority(eg. High, Medium, Low) is the task you would like to delete?\n")
        if priority.capitalize() == "High":
            print(todos["High"])
            task = int(input("Which task? (Please type the corresponding placement number (eg. 1,2,3): \n"))
            del todos["High"][task -1]
            print(todos.items())
            
        if priority.capitalize() == "Medium":
            print(todos["Medium"])
            task = int(input("Which task? (Please type the corresponding placement number (eg. 1,2,3): \n"))
            del todos["Medium"][task -1]
            print(todos.items())
            
        if priority.capitalize() == "Low":
            print(todos["Low"])
            task = int(input("Which task? (Please type the corresponding placement number (eg. 1,2,3): \n"))
            del todos["Low"][task -1]
            print(todos.items())
            
    if question == "3":
        for key, value in todos.items():
            print(f"{key}\n{value}")
        
    if question.lower() == "q":
        break
