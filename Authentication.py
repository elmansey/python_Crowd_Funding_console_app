
from Validation import egyption_phone_number_validator , email_validator ,password_validator
from Store_data import store_data_in_txt_file , search_for_user_in_file , generateId
from projects_menu import showProjectMenu


def register():
    while True:
        fname = input(" Please enter your first name: ")
        if not fname :
            print(" invalid input empty value :")
        else:
            break

    while True:
        lname = input(" Please enter your last name: ")
        if not lname :
            print(" invalid input empty value :")
        else:
            break
        
    while True:
        email = input(" Please enter your email: ")
        if not email_validator(email):
            print(" invalid input please enter valid email:")
        else:
            break

    while True:
        password = input(" Please enter your password: ")
        if not password_validator(password):
            print(" invalid input the password can not be less than 3 charachter :")
        else:
            break

    while True:
        confirm_password = input(" Please confirm your password must equle with password : ")
        if not password_validator(confirm_password):
            print(" invalid input the password can not be less than 3 charachter :")
        elif password == confirm_password:
            break

    while True:
        phone = input(" Please enter your phone number : ")
        if not egyption_phone_number_validator(phone):
            print(" invalid input please enter valid phone :")
        else:
            break

    id = generateId()
    userInfo = f"{id}:{fname}:{lname}:{email}:{password}:{phone}\n"  
    file = 'users.txt'      
    if store_data_in_txt_file(file,userInfo):
        print(" registed successfully :D")
    else:
        print(" something has happened please try again ")






def login ():
    while True:
        email = input(" Please enter your email: ")
        if not email_validator(email):
            print(" invalid input please enter valid email:")
        else:
            break

    while True:
        password = input(" Please enter your password: ")
        if not password_validator(password):
            print(" invalid input the password can not be less than 3 charachter :")
        else:
            break

    user = search_for_user_in_file(email,password)
    if user:
        id = user.strip('\n').split(":")[0]
        name = user.strip('\n').split(":")[1]
        global authUser
        authUser = user
        print(f" Welcome {name} :D")
        showProjectMenu()
    else:
        print(" error in email or password !")