feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    feet_inches = feet_inches.split(" ")

    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    feet = feet + inches / 12

    meters = feet / 3
    
    return meters

parsed = parse(feet_inches)

print("Meters:" + str(convert(parsed["feet"], parsed["inches"])))