def get_average():
    with open("App1-ToDo/bonus/files/data.txt", "r") as file:
        data = file.readlines()
    
    values = data[1:]
    values = [float(value) for value in values]
    
    average = sum(values) / len(values)
    return average

average = get_average()
print(average)