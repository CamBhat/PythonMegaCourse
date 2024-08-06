date = input("Enter today's date (YYYY-MM-DD): ")
mood = input("How do you rate your mood today from 1 to 10? ")
entry = input("Let your thoughts flow:\n")

with open(f"app1/journal/{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(entry)