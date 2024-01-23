# MODULE TO View MARKSHEETS
"""
This module contains 1 method :     FetchMarkSheet(arg1, arg2) 

arg1 : Student's name
arg2 : srtudent's Roll No

-> then it combines & forms the File Name.
-> Opens the text file with the same name in the directory.
-> reads the data and displays

"""

def FetchMarkSheet(SName,SRollNo):                                   #method for fetching marksheet
    print("\n\n")

    FName=SName + " " + SRollNo + ".txt"                      # Concatanating Strings to mmake file name

    try:
        with open(FName, 'r') as ViewHandler:               # Opening Students marksheet
            data=ViewHandler.read()                         # Reading and storing data
            print(data)                                     # Printing Marksheet

    except NameError as NE:                                      #exception handeling for NameErrors
        print("\nERROR...!!!", NE, "\n")
    except ValueError as VE:                                     #exception handeling for ValueErrors
        print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
    except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
        print("\nNO FILE FOUND ...!!!", FNE, "\n")
    except KeyboardInterrupt:                                    #exception handeling for KeyboardInterrupt 
        print("\n\nINTERRUPTION BY USER  --  OPERATION ABORTED")