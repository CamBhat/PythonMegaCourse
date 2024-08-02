# Initial list to be manipulated
file_read = open("App1-ToDo/todos.txt", "r")
todos = file_read.readlines()

file_write = open('App1-ToDo/todos.txt', "w")

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
            
            file_write.writelines(todos)
            
        # Shows To-Do list
        case 'show':
            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo}")
                
        # Edits an item in the To-Do list
        case 'edit':
            number = int(input("Number of todo to edit: "))
            
            if 1 <= number <= len(todos):
                new = input("Enter editted todo: ") + "\n"
                print(todos[number - 1], "has been replaced with", new)
                todos[number - 1] = new 
            else:
                print("Index of todo not found")
            file_write.writelines(todos)
                
        # Completes and removes an item from To-Do list
        case 'complete':
            number = int(input("Number of todo to complete: "))
            
            if 1 <= number <= len(todos):
                print(todos[number - 1], "has been completed")
                todos.pop(number - 1)
            else:
                print("Index of todo not found")
            file_write.writelines(todos)
                
        # Ends the program
        case 'exit':
            break
        
        # Edge case of unknown commands
        case foo:
            print("Unknown command")

# Closes files
file_read.close()
file_write.close()

# Exit print
print("Bye!")