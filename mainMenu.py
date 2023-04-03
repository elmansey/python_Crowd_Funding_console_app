
from Authentication import login , register



def showMenu():
    while True:
        print(" 1 ) Login \n 2 ) Register \n 3 ) Exit \n")
        choise = int(input(" Please Enter Your Choise [ 1-2-3 ]: "))
        if choise == 1:
            login()
            break
        elif choise == 2:
            register()
            break
        elif choise == 3:
            print(" goodby :D")
            break
        else:
            print(" invalid choise please choise from [1-2-3]")

            
showMenu()