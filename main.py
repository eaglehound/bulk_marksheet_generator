# MAIN Module 
"""
Main Module 

It invokes 3 other modules:
    1)  myMSGenerator   :   for generating Marksheet in bulk using MSMaker() method
    2)  myMSViewer      :   For viewing marksheet using FetchMarkSheet() method
    3)  myMSCorrector   :   For making corrections in exixting marksheet using CorrectorMS() method
"""

import myMSGenerator        # Importing Module - Marksheet generator 
import myMSViewer           # Importing Module - Marksheet Viewer
import myMSCorrector

print("\n\n----------------------------------------------------------")
print("------  SOFTWARE TO GENERATE & CORRECT MARKSHEETS  -------")
print("----------------------------------------------------------")


runner = True       #programm runner
    
while(runner==True):            # loop for showing menu
    print("\n\n-------------------------  MENU  -------------------------")
    print(" Press >>  1  << for Generating Marksheets.")
    print(" Press >>  2  << for Correcting Marksheets.")
    print(" Press >>  3  << for Viewing Marksheets.")
    print(" Press >>  0  << for Exiting the software.")
    print("----------------------------------------------------------\n")

    try:
        ch =str(input(">>> ENTER YOUR CHOICE : "))                  # asking for choice

        if(ch== "1"):
            myMSGenerator.MSMaker()         #Calling Function for Generating Marksheets in Bulk through myMSGenerator Module 

        elif(ch== "2"):
            myMSCorrector.CorrectorMS()     #Calling Function for Correcting Marksheets through myMSCorrector Module

        elif(ch== "3"):
            SName=input("\nEnter the student's Name : ")         #Getting Student's Name
            SRollNo =input("ENter the student's Roll No : ")     #Getting Student's Roll No
            myMSViewer.FetchMarkSheet(SName,SRollNo)             #Calling Function for Viewing Marksheets through myMSViewer Module

        elif(ch== "0"):
            print("\n\nEXITING THE PROGRAMME......... GOODBYE & GODSPEED\n\n")
            runner = False

        else:
            print("\nINVALID CHOICE.....!    Choose Again")

    except NameError as NE:                                      #exception handeling for NameErrors
        print("\nERROR...!!!", NE, "\n")
    except ValueError as VE:                                     #exception handeling for ValueErrors
        print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
    except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
        print("\nERROR -- NO FILE FOUND ...!!!", FNE, "\n")
    except KeyboardInterrupt:                                    #exception handeling for KeyboardInterrupt 
            print("\n\nINTERRUPTION BY USER  --  SOFTWARE TERMINATED")
            print("\nThank you for using --  GOODBYE AND GODSPEED\n")
            runner = False
        
