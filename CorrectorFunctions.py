from datetime import date
import os       #Importing OS module for using rename() method

##########################################################################################################################################
""" 
Function to Update Name + Renaming The File Name 

Function : NNameCorrector(arg1, arg2, arg3)

Takes:
    arg1  :  FName       :  File Name
    arg1  :  searchText  :  string text to be searched and updated (Previous Name)
    arg1  :  replaceText :  tring text to be updated with (New Name)

    Renames the file after updating the Name in Marksheet

    further if also calls DateCorrector() as after making changes New Issue Date has to be assigned

"""

def NameCorrector(FName, searchText, replaceText):
    try:
        with open(FName, 'r') as SearchHandler:              # Opening Studen'ts marksheet
            data= SearchHandler.read()

        if searchText not in data:                          #returning False if Data is not present in the marksheet file
            print( "\nDATA NOT PRESENT....")
            return False

        data = data.replace(searchText, replaceText)     #Replacing the text

        with open(FName, 'w') as NameChangeHandler:             # Svaing Data to Student's marksheet 
            NameChangeHandler.write(data)
        
        DateCorrector(FName)
        print("\n Date of Issue also updated.....")
                        
        OldName = FName
        ListOldName=FName[:-4].split(sep=" ")
        NewName = replaceText + " " + ListOldName[-1] + ".txt"

        if os.path.isfile(NewName):                         #Checking if file already exists
            print("\nThe file already exists")
        else:
            # Rename the file
            os.rename(OldName, NewName)
            print("\nFile Name Also Updated......")
            return True

    except NameError as NE:                                      #exception handeling for NameErrors
        print("\nERROR...!!!", NE, "\n")
    except ValueError as VE:                                     #exception handeling for ValueErrors
        print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
    except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
        print("\nNO FILE FOUND ...!!!", FNE, "\n")
    except PermissionError as PE:
        print("Prompted Data NOT FOUND......", PE, "\n")

##########################################################################################################################################



##########################################################################################################################################
# Function to Update Roll No + Renaming The File Name
""" 
Function to Update Roll No + Renaming The File Name

Function : RollNoCorrector(arg1, arg2, arg3)

Takes:
    arg1  :  FName       :  File Name
    arg1  :  searchText  :  string text to be searched and updated (Previous Roll No)
    arg1  :  replaceText :  tring text to be updated with (New Roll No)

    Renames the file after updating the Roll No in Marksheet 

    further if also calls DateCorrector() as after making changes New Issue Date has to be assigned
"""

def RollNoCorrector(FName,searchText, replaceText):
    try:
        with open(FName, 'r') as SearchHandler:              #Opening Studen'ts marksheet
            data= SearchHandler.read()

        if searchText not in data:                          #returning False if Data is not present in the marksheet file
            print( "\nDATA NOT PRESENT....")
            return False

        data = data.replace(searchText, replaceText)     #Replacing the text

        with open(FName, 'w') as NameChangeHandler:             #Svaing Data to Student's marksheet 
            NameChangeHandler.write(data)

        DateCorrector(FName)
        print("\n Date of Issue also updated.....")

        OldName = FName
        ListOldName=FName[:-4].split(sep=" ")
        str1=""
        for x in ListOldName[:-1]:
            str1 = str1 + x + " "
            print(str1, type(str1))

        NewName = str1 + replaceText + ".txt"

        if os.path.isfile(NewName):                         #Checking if file already exists
            print("\nThe file already exists")
        else:
            # Renaming the file
            os.rename(OldName, NewName)
            print("\nFile Name Also Updated......")

    except NameError as NE:                                      #exception handeling for NameErrors
        print("\nERROR...!!!", NE, "\n")
    except ValueError as VE:                                     #exception handeling for ValueErrors
        print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
    except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
        print("\nNO FILE FOUND ...!!!", FNE, "\n")
    except PermissionError as PE:
        print("Prompted Data NOT FOUND......", PE, "\n")

##########################################################################################################################################



##########################################################################################################################################
# Function to Update other fields

""" 
Function to Update programme Name, Year of Award, Subject Marks, Year Of Passing, Dtae Of Issue,Signing Authority

Function : FieldCorrector(arg1, arg2, arg3)

Takes:
    arg1  :  FName       :  File Name
    arg1  :  searchText  :  string text to be searched and updated (Previous Roll No)
    arg1  :  replaceText :  tring text to be updated with (New Roll No) 

    further if also calls DateCorrector() as after making changes New Issue Date has to be assigned

"""

def FieldCorrector(FName, searchText, replaceText):
    try:    
        with open(FName, 'r') as SearchHandler:              # Opening Studen'ts marksheet
            data= SearchHandler.read()

            if searchText in data:
                data = data.replace(searchText, replaceText)     #Replacing the text
                    
            else:
                print( "\nDATA NOT PRESENT....")
                return(False)                               #returning False if Data is not present in the marksheet file
                    

        with open(FName, 'w') as ReplaceHandler:             # Svaing Data to Student's marksheet 
            ReplaceHandler.write(data)
        
        DateCorrector(FName)
        print("\n Date of Issue also updated.....")

        return(True)

    except NameError as NE:                                      #exception handeling for NameErrors
        print("\nERROR...!!!", NE, "\n")
    except ValueError as VE:                                     #exception handeling for ValueErrors
        print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
    except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
        print("\nNO FILE FOUND ...!!!", FNE, "\n")
    except PermissionError as PE:
        print("Prompted Data NOT FOUND......", PE, "\n")

##########################################################################################################################################



##########################################################################################################################################
# Function to Update Dates 

""" 
Function to Dtae Of Issue

function : DateCorrector(arg1)
Takes:
    arg1  :  FName       :  File Name

    also uses date.today() method from date Module
"""


def DateCorrector(FName):
    try:
        with open(FName, 'r') as DateHandler:               # Opening Students marksheet
            dateFinder=DateHandler.read()                         # Reading and stored data
                                       
            x1= dateFinder.split("\n")
            x2= x1[-8].split(" ")
            PrevDate = x2[-1]                              #setting searchText = previous date in marksheet
            NewDate = str(date.today())                  #setting replaceText = Current date through date Module

                    
            print("\nPrevious Date was : ", PrevDate)
            print("Date to be Updated : ", NewDate)
            dateFinder = dateFinder.replace(PrevDate, NewDate)     #Replacing the text
                
        with open(FName, 'w') as ReplaceHandler:             # Svaing Data to Student's marksheet 
            ReplaceHandler.write(dateFinder)

    except NameError as NE:                                      #exception handeling for NameErrors
        print("\nERROR...!!!", NE, "\n")
    except ValueError as VE:                                     #exception handeling for ValueErrors
        print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
    except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
        print("\nNO FILE FOUND ...!!!", FNE, "\n")
    except PermissionError as PE:
        print("Prompted Data NOT FOUND......", PE, "\n")

##########################################################################################################################################