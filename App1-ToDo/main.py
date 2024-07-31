todos = ['Test1', 'Test2', 'Test3']

while True:
    user_action = input("Type add, show, edit, delete, or exit: ")

    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for x in range(len(todos)):
                print (x + 1, "-", todos[x])
        case 'edit':
            number = int(input("Number of todo to edit: "))
            
            if 1 <= number <= len(todos):
                new = input("Enter editted todo: ")
                print(todos[number - 1], "has been replaced with", new)
                todos[number - 1] = new 
            else:
                print("Index of todo not found")
        case 'delete':
            number = int(input("Number of todo to delete: "))
            
            if 1 <= number <= len(todos):
                print(todos[number - 1], "has been delete")
                del todos[number - 1]
            else:
                print("Index of todo not found")
        case 'exit':
            break
        case foo:
            print("Unknown command")

print("Bye!")