import time
from Store_data import store_data_in_txt_file , get_all_data_from_file , generateId , search_for_project_by_id ,deleteElementFromFile, store_rows_in_txt_file
from Validation import date_formate_validation



def create():

    while True:
        title  = input(" Please enter the project title: ")
        if not title  :
            print(" invalid input empty value :")
        else:
            break
    
    details = input(" Please enter the project details: ")

    while True:
        total_target = input(" Please enter the total target for this project: ")
        if not total_target or not total_target.isdigit() :
            print(" invalid input can not be string / empty value : ")
        else:
            break


    while True:
        start_date  =  input(" Please enter the start date for this project formate ['00/00/0000'] : ")
        if not date_formate_validation(start_date):
            print(" invalid input please enter valid formate ['12/12/2022'] : ")
        else:
            break

    while True: 
        end_date  =  input(" Please enter the end date for this project formate ['00/00/0000'] : ")
        if not date_formate_validation(end_date):
            print(" invalid input please enter valid formate ['12/12/2022'] : ")
        else:
            break

        
    project_id = generateId()
    # userId = auth().strip('\n').split(":")[0]
    file = 'project.txt'
    project = f"{project_id}:{title}:{details}:{total_target}:{start_date}:{end_date}\n"
    if store_data_in_txt_file(file,project):
        print(" Project added successfully :D")
    else:
        print(" something has happened please try again ")




def get_all_projects():
    file= 'project.txt'
    projects = get_all_data_from_file(file)
    return projects



def deleteProject():
    projectId = input(" Please enter the project id you wont to delete it : ")
    if not search_for_project_by_id(projectId):
        print(" something was happened please try again ")
    else:
        project = search_for_project_by_id(projectId)
        file = 'project.txt'
        if deleteElementFromFile(file,project):
            print(" project deleted succesfully ")
        else:
            print(" something was happend please try again ")




def edit_project_by_id():
    projectId = input(" Please enter the project id you wont to update it : ")
    if not search_for_project_by_id(projectId):
        print(" something was happened please try again ")
    else:
        oldProject = search_for_project_by_id(projectId)
        project = oldProject
        column = input(" please enter the colum want to update it  \n [ title - details - total_target - start_date - end_date ] : ")
       
        while True:
            if   column == 'title':
                while True:
                    title  = input(" Please enter the new project title: ")
                    if not title :
                        print(" invalid input empty value :")
                    else:
                        projectSplit = project.split(":")
                        projectSplit[1] = title
                        seperator = ':'
                        project = seperator.join(projectSplit)
                        break
                break

            elif column == 'details':
                details = input(" Please enter the project details: ")
                projectSplit = project.split(":")
                projectSplit[2] = details
                seperator = ':'
                project = seperator.join(projectSplit)
                break
            elif column == 'total_target':
                while True:
                    total_target = input(" Please enter the new total target for this project: ")
                    if not total_target or not total_target.isdigit() :
                        print(" invalid input can not be string / empty value : ")
                    else:
                        projectSplit = project.split(":")
                        projectSplit[3] = total_target
                        seperator = ':'
                        project = seperator.join(projectSplit)
                        break
                break
            elif column == 'start_date':
                while True:
                    start_date  =  input(" Please enter the new start date for this project formate ['00/00/0000'] : ")
                    if not date_formate_validation(start_date):
                        print(" invalid input please enter valid formate ['12/12/2022'] : ")
                    else:
                        projectSplit = project.split(":")
                        projectSplit[4] = start_date
                        seperator = ':'
                        project = seperator.join(projectSplit)
                        break
                
                break
            elif column == 'end_date':
                    while True: 
                        end_date  =  input(" Please enter the new end date for this project formate ['00/00/0000'] : ")
                        if not date_formate_validation(end_date):
                            print(" invalid input please enter valid formate ['12/12/2022'] : ")
                        else:
                            projectSplit = project.split(":")
                            projectSplit[5] = end_date
                            seperator = ':'
                            project = seperator.join(projectSplit)
                            break
                    break
            else:
                print(" invalid input please enter valid choise")

        file = 'project.txt'
        projects = get_all_projects()
        projects.append(project)
        if store_rows_in_txt_file(file,projects):
            print(" project updated succesfully ")
            deleteElementFromFile(file,oldProject)
        else:
            print(" something was happend please try again ")












# def search_for_a_project():
#     while True:
#         start_date  =  input(" Please enter the start date for this project formate ['00/00/0000'] : ")
#         if not date_formate_validation(start_date):
#             print(" invalid input please enter valid formate ['12/12/2022'] : ")
#         else:
#             break

#     while True: 
#         end_date  =  input(" Please enter the end date for this project formate ['00/00/0000'] : ")
#         if not date_formate_validation(end_date):
#             print(" invalid input please enter valid formate ['12/12/2022'] : ")
#         else:
#             break


#         print(get_all_projects())
#         # for project in projects:
#         #       print(project)
#         #     startData = project.strip("\n").split(":")[4]
#         #     endData = project.strip("\n").split(":")[5]
#         #     print(type(startData))
#         #     print(type(endData))
#         #     print(type(start_date))
#         #     print(type(end_date))
#         #     # if start_date == startData and end_date == endData:
#         #     #     print(project)
#         # return True
        