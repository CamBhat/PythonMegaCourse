try:

    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    exit("That looks like a square") if width == length else print(width * length)
    
except ValueError:
    print("Please enter a number.")