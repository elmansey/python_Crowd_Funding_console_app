
import time

def generateId():
    return round(time.time())


def store_data_in_txt_file(file,data):
    try:
        fileobj = open(file,'a')
    except Exception as e :
        print(e)
        return False
    else:
        fileobj.write(data)
        fileobj.close()
        return True

def store_rows_in_txt_file(file,data):
    try:
        fileobj = open(file,'w')
    except Exception as e :
        print(e)
        return False
    else:
        fileobj.writelines(data)
        fileobj.close()
        return True



def get_all_data_from_file(file):
    try:
        fileobj = open(file,'r')
    except Exception as e :
        print(e)
        return False
    else:
        res = fileobj.readlines()
        fileobj.close()
        return res



def search_for_user_in_file(email,password):
    file = 'users.txt'
    allUsers = get_all_data_from_file(file)

    for user in allUsers:
        userEmail = user.strip('\n').split(":")[3]
        userPassword = user.strip('\n').split(":")[4]
        if userEmail == email and userPassword == password:
            return user


def search_for_project_by_id(project_id):
    file = 'project.txt'
    projects = get_all_data_from_file(file)

    for project in projects:
        id = project.strip('\n').split(":")[0]
        if id == project_id:
            return project
        
    return False


def deleteElementFromFile(file,element):
    projects = get_all_data_from_file(file)
    projects.remove(element)
    return store_rows_in_txt_file(file,projects)



# def updateElementFromFile(file,element):

