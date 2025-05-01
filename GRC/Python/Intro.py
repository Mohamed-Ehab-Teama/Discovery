# UserName => 8-20 characters, 1 UpperCase, 1 number, Special Character (!#$_), contain @, end with the ".discovery"

def check_userName( userName ):
    errors = []
    
    # Check if the userName is empty
    if len(userName) <= 0 :
        errors.append("User Name cannot be empty")
        
    # Check username Length
    if len(userName) < 8 or len(userName) > 20:
        errors.append("User name must be 8-20 characters")
        
    # check if UserName contains an uppercase
    upper = False
    for u in userName:
        if u.isupper():
            upper = True
    if upper == False:
        errors.append("User Name must contain an uppercase")
        
    # check if UserName contains a number
    number = False
    for n in userName:
        if n.isdigit():
            number = True
    if number == False:
        errors.append("User Name must contain a number")

    # Check if the user name contains !#$_
    specialChar = False
    for s in userName:
        if s in ("!#$_"):
            specialChar = True      
    if specialChar == False:
        errors.append("User Name must contain a Special Character")
    
    # Check if the user name contains @
    containt_at = False
    for a in userName:
        if a == '@':
            containt_at = True      
    if containt_at == False:
        errors.append("User Name must contain an @")
        
    # Check if userName endswith .discovery
    # if userName[-10:] != '.discovery':
    #     errors.append("User Name must ends with .discovery ")
    if not userName.endswith(".discovery"):
        errors.append("User Name must ends with .discovery ")
    
    # Check if Acceoted or not
    if not errors:
        print("Accepted")
    else:
        # for e in errors:
        #     print(e)
        print(" ".join(errors))
        print("Rejected")
        
check_userName("Ali_ee@10.discovery")