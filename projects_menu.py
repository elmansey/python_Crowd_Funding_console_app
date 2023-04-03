from Projects import create , get_all_projects,deleteProject  ,edit_project_by_id

def showProjectMenu():
    while True:
        print(" 1 ) create project  \n 2 ) all projects  \n 3 ) edit project \n 4 ) delete project \n 5 ) search for a project \n 6 ) Exit " )
        choise = int(input(" Please Enter Your Choise [ 1-6 ]: "))
        if choise == 1:
            create()
        elif choise == 2:
            projects = get_all_projects()
            for project in projects :
                project = project.strip("\n")
                print(" ",project)
        elif choise == 3:
            edit_project_by_id()
        elif choise == 4:
            deleteProject()
        elif choise == 5:
            # search_for_a_project()
            break
        elif choise == 6:
            print("goodby :D")
            break
        else:
            print("invalid choise please choise from [1-2-3]")

            
