import re



def date_formate_validation(date):
    regex= "^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$"
    if re.match(regex,date):
        return True
    else:
        return False


def email_validator(email):
    regex = '^\w+[\w\.-]*@\w+[\w\.-]+\.\w{2,}$'
    if re.match(regex,email):
        return True
    else:
        return False


def egyption_phone_number_validator(phone):
    regex = "^(01)[0125][0-9]{8}$"
    if re.match(regex,phone):
        return True
    else:
        return False
    

def password_validator(password):
    if len(password) >= 3:
        return True
    else:
        return False
