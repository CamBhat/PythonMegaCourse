# Initial list to be manipulated
file = open("App1-ToDo/todos.txt", "r")
todos = file.readlines()
file.close()

while True:
    
    # Actions a user can take
    user_action = input("Type add, show, edit, complete, or exit: ")

    # Strips spaces
    user_action = user_action.strip()

    # Does different actions based on user's input
    match user_action:
        
        # Adds item to To-Do list
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            todos.append(todo)
            
            file = open("App1-ToDo/todos.txt", "w")
            file.writelines(todos)
            file.close()
            
        # Shows To-Do list
        case 'show':
            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo.strip("\n")}")
                
        # Edits an item in the To-Do list
        case 'edit':
            number = int(input("Number of todo to edit: "))
            
            if 1 <= number <= len(todos):
                new = input("Enter editted todo: ") + "\n"
                print(todos[number - 1], "has been replaced with", new)
                todos[number - 1] = new 
            else:
                print("Index of todo not found")

            file = open("App1-ToDo/todos.txt", "w")
            file.writelines(todos)
            file.close()
                
        # Completes and removes an item from To-Do list
        case 'complete':
            number = int(input("Number of todo to complete: "))
            
            if 1 <= number <= len(todos):
                print(todos[number - 1], "has been completed")
                todos.pop(number - 1)
            else:
                print("Index of todo not found")

            file = open("App1-ToDo/todos.txt", "w")
            file.writelines(todos)
            file.close()
                
        # Ends the program
        case 'exit':
            break
        
        # Edge case of unknown commands
        case foo:
            print("Unknown command")

# Exit print
print("Bye!")