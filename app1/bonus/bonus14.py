from functions14 import parse, convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

print("Meters:" + str(convert(parsed["feet"], parsed["inches"])))