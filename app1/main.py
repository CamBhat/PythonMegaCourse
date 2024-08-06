from app1.modules.functions import *
import time

current_time = time.strftime("%Y-%m-%d %H:%M:%S")

print(f"It is currently {current_time}.")

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
        show_todos()
                
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