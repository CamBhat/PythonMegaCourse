# Initial list to be manipulated
with open("App1-ToDo/todos.txt", "r") as file:
    todos = file.readlines()

while True:
    
    # Actions a user can take
    user_action = input("Type add, show, edit, complete, or exit: ")

    # Strips spaces
    user_action = user_action.strip()
        
    # Adds item to To-Do list
    if user_action.startswith('add'):
        
        if (len(user_action) <= 4):
            todo = input("Enter a todo: ") + "\n"

            todos.append(todo)
                
            with open("App1-ToDo/todos.txt", "w") as file:
                file.writelines(todos)
        
        else:
            todo = user_action.strip("add ")
            todos.append(todo)
                
            with open("App1-ToDo/todos.txt", "w") as file:
                file.writelines(todos)
            
        # Shows To-Do list
    elif user_action.startswith('show'):
        for index, todo in enumerate(todos):
            print(f"{index + 1} - {todo.strip("\n")}")
                
    # Edits an item in the To-Do list
    elif user_action.startswith('edit'):
        
        try:
        
            if (len(user_action) <= 4):
                number = int(input("Number of todo to edit: "))
                    
                if 1 <= number <= len(todos):
                    new = input("Enter editted todo: ") + "\n"
                    print(todos[number - 1].strip("\n"), "has been replaced with", new.strip("\n"))
                    todos[number - 1] = new 
                else:
                    print("Index of todo not found")

                with open("App1-ToDo/todos.txt", "w") as file:
                    file.writelines(todos)
                    
            else:
                number = int(user_action.strip("edit "))
                
                if 1 <= number <= len(todos):
                    new = input("Enter editted todo: ") + "\n"
                    print(todos[number - 1].strip("\n"), "has been replaced with", new.strip("\n"))
                    todos[number - 1] = new 
                else:
                    print("Index of todo not found")

                with open("App1-ToDo/todos.txt", "w") as file:
                    file.writelines(todos)
        
        except ValueError:
            print("Your command is not valid.")
            continue
                
                
    # Completes and removes an item from To-Do list
    elif user_action.startswith('complete'):
        if (len(user_action) <= 8):
            number = int(input("Number of todo to complete: "))
                
            if 1 <= number <= len(todos):
                print(todos[number - 1].strip("\n"), "has been completed")
                todos.pop(number - 1)
            else:
                print("Index of todo not found")

            with open("App1-ToDo/todos.txt", "w") as file:
                file.writelines(todos)
                
        else:
            number = int(user_action.strip("complete "))
            
            if 1 <= number <= len(todos):
                print(todos[number - 1].strip("\n"), "has been completed")
                todos.pop(number - 1)
            else:
                print("Index of todo not found")

            with open("App1-ToDo/todos.txt", "w") as file:
                file.writelines(todos)
                
    # Ends the program
    elif user_action.startswith('exit'):
        break
        
    # Edge case of unknown commands
    else:
        print("Unknown command")

# Exit print
print("Bye!")