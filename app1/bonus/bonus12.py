feet_inches = input("Enter feet and inches: ")

feet_inches = feet_inches.split(" ")

feet = float(feet_inches[0])
inches = float(feet_inches[1])

feet = feet + (inches / 12)

meters = feet / 3

print("Meters:" + str(meters))