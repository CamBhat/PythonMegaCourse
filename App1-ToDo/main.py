# Initial list to be manipulated
with open("App1-ToDo/todos.txt", "r") as file:
    todos = file.readlines()

def write_todos(todos):
    with open("App1-ToDo/todos.txt", "w") as file:
        file.writelines(todos)

def add_todo(user_action):
    if (len(user_action) <= 4):
        todo = input("Enter a todo: ") + "\n"
        todos.append(todo)
        write_todos(todos)
        
    else:
        todo = user_action[4:] + "\n"
        todos.append(todo) 
        write_todos(todos)

def edit_todo(user_action):
    try:
        if (len(user_action) <= 4):
            number = int(input("Number of todo to edit: "))    
        else:
            number = int(user_action[4:]) 
    except ValueError:
        print("Your command is not valid.")
        return
            
    try:
        new = input("Enter editted todo: ") + "\n"
        print(todos[number - 1].strip("\n"), "has been replaced with", new.strip("\n"))
        todos[number - 1] = new
        write_todos(todos)
    except IndexError:
        print("Index of todo not found.")
        return

def complete_todo(user_action):
    number = 0
    
    try:
        if (len(user_action) <= 8):
                number = int(input("Number of todo to complete: "))    
        else:
            number = int(user_action[8:])
    except ValueError:
        print("Your command is not valid.")
        return

    try:
        print(todos[number - 1].strip("\n"), "has been completed")
        todos.pop(number - 1)
        write_todos(todos)
    except IndexError:
        print("Index of todo not found.")
        return

while True:
    
    # Actions a user can take
    user_action = input("Type add, show, edit, complete, or exit: ")

    # Strips spaces
    user_action = user_action.strip()
        
    # Adds item to To-Do list
    if user_action.startswith('add'):
        add_todo(user_action)
            
    # Shows To-Do list
    elif user_action.startswith('show'):
        for index, todo in enumerate(todos):
            print(f"{index + 1} - {todo.strip("\n")}")
                
    # Edits an item in the To-Do list
    elif user_action.startswith('edit'):
        edit_todo(user_action)
                        
    # Completes and removes an item from To-Do list
    elif user_action.startswith('complete'):
        complete_todo(user_action)
                
    # Ends the program
    elif user_action.startswith('exit'):
        print("Bye!")
        break
        
    # Edge case of unknown commands
    else:
        print("Unknown command")