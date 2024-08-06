password = input("Enter new password: ")

result = True

if len(password) < 8:
    result = False
    
contains_digit = False
for i in password:
    if i.isdigit():
        contains_digit = True
        
if contains_digit == False:
    result = False
    
contains_uppercase = False
for i in password:
    if i.isupper():
        contains_uppercase = True
        
if contains_uppercase == False:
    result = False
    
if result == False:
    print("Weak password")
    
else:
    print("Strong password")