def check_crendentials(userName, password):
    userNameErrors = []
    passwordErrors = []

    def check_userName(userName):
        # Check if userName is empty
        if len(userName) <= 0:
            userNameErrors.append("UserName Cannot be Empty")
        else:
            print("UserName Length Passed")

        # Check if userName Contains upperCase
        userUpperCase = False
        for i in userName:
            if i.isupper():
                print("UpperCase Rule Passed")
                userUpperCase = True
                break
        if userUpperCase != True:
            userNameErrors.append("UserName must contain an UpperCase")

        # Check if userName Contains underScore
        if "_" in userName:
            print("UnerScore Rule Passed")
        else:
            userNameErrors.append("UserName must contain an UnerScore")
        
        # Check if userName Contains @
        if "@" in userName:
            print("@ Sympol Rule Passed")
        else:
            userNameErrors.append("UserName must contain @ Symbol")
        
        # Check if userName endsWith .discovery
        if userName.endswith('.discovery'):
            print(".discovery Rule Passed")
        else:
            userNameErrors.append("UserName must end With .discovery")
    
    def check_password(password):
        # Check if password is empty
        if len(password) <= 0:
            passwordErrors.append("password Cannot be Empty")
        else:
            print("password Length Passed")

        # Check if password Contains upperCase
        passwordUpperCase = False
        for i in password:
            if i.isupper():
                print("UpperCase Rule Passed")
                passwordUpperCase = True
                break
        if passwordUpperCase != True:
            passwordErrors.append("password must contain an UpperCase")
        
        # Check if password contains @#!
        passwordSympol = False
        for p in password:
            if p in '!@#':
                passwordSympol = True
                print("Password Contains @ or ! or # Rule Passed")
                break
        if passwordSympol != True:
            passwordErrors.append("password must contain  @ or ! or #")       
        
        # Check if password contains Numbers
        passwordNumber = False
        for p in password:
            if p.isnumeric():
                passwordNumber = True
                print("Password Contains Number Rule Passed")
                break
        if passwordNumber != True:
            passwordErrors.append("password must contain a number")       
                
    # Call the functions
    check_userName(userName)
    check_password(password)
    
    # Print All UserName Errors
    for us in userNameErrors:
        print(us)
        
    print()
    
    # Print All UserName password
    for pa in passwordErrors:
        print(pa)
    
    print()
    
    # Check if the Credentials are Valid
    if len(userNameErrors) == 0 and len(passwordErrors) == 0:
        print('Success Registration')
    else:
        print('Registration Failed')
        
check_crendentials('hello', 'hello')
check_crendentials('Hello_@123.discovery', 'hellO@1255745')