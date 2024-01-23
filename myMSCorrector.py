#Module for Making Changes in Marksheets.
"""
This Module Contains 1 method : CorrectorMS()

-> Further it calls the other Corrector functions from the Module CorrectorFunctions given below :
            1)  CorrectorFunctions.NameCorrector(FName, searchText, replaceText)
            2)  CorrectorFunctions.RollNoCorrector(FName, searchText, replaceText)
            3)  CorrectorFunctions.FieldCorrector(FName, searchText, replaceText)
            4)  CorrectorFunctions.DateCorrector(FName)
"""
import os                     
import CorrectorFunctions
from datetime import date

def CorrectorMS():                                       #method for fetching marksheet 
    CRunner=True

    while(CRunner == True):
        print("\n\n------------------------- CORRECTOR MENU  -------------------------")
        print("Press  >> 1 <<  to make changes in Name")
        print("Press  >> 2 <<  to make changes in Roll No")
        print("Press  >> 3 <<  to make changes in Programme")
        print("Press  >> 4 <<  to make changes in Subject Marks")
        print("Press  >> 5 <<  to make changes in Year of Passing")
        print("Press  >> 6 <<  to make changes in Date of Issue")
        print("Press  >> 7 <<  to make changes in Signing Authority")
        print("Press  >> 0 <<  to ABORT")
        print("--------------------------------------------------------------------\n\n")

        Cch= str(input("\n>>> ENTER YOUR CHOICE : "))

        print("\n\nPLEASE ENTER THE DETAILS ABOUT RECORD :")
        SName=input("\nEnter the student's name : ")         #Getting Student's Name
        SRollNo =input("ENter the student's Roll No : ")     #Getting Student's Roll No
         
        FName=SName + " " + SRollNo + ".txt"                      # Concatanating Strings to mmake file name


        try :
            if(Cch=="1"):
                result = True

                print("\nENTER THE DETAILS FOR CORRECTION....: ")
                searchText = input("\nEnter the Previous Full Name : ")  #getting the Incorrect NAME to be replaced
                replaceText = input("Enter the New Full Name : ")        #getting the Correct NAME to be replaced with
                result = CorrectorFunctions.NameCorrector(FName, searchText, replaceText)

                if(result == True):
                    print("\nNAME Updated Successfuly.....")
                if(result == False):
                    print("\nNAME couldn't be Updated.....")

            elif(Cch=="2"):
                result = True

                print("\nENTER THE DETAILS FOR CORRECTION....: ")
                searchText = input("\nEnter the Previous Roll No : ")  #getting the Incorrect ROLL NO to be replaced
                replaceText = input("Enter the New Roll No : ")        #getting the Correct ROLL No to be replaced with
                result = CorrectorFunctions.RollNoCorrector(FName, searchText, replaceText)

                if(result == True):
                    print("\nROLL NO Updated Successfuly.....")
                if(result == False):
                    print("\nROLL NO couldn't be Updated.....")

            elif(Cch=="3"):
                result= True
                
                print("\nENTER THE DETAILS FOR CORRECTION....: ")
                searchText = input("\nEnter the Previous Programme Name : ")  #getting the Incorrect PROGRAMME NAME to be replaced
                replaceText = input("Enter the New Programme Name : ")        #getting the Correct PROGRAMME NAME to be replaced with
                result = CorrectorFunctions.FieldCorrector(FName, searchText, replaceText)

                if(result == True):
                    print("\nPROGRAMME NAME Updated Successfuly.....")
                if(result == False):
                    print("\nPROGRAMME NAME couldn't be Updated.....")

            elif(Cch=="4"):
                result= True
                
                print("\nENTER THE DETAILS FOR CORRECTION....: ")
                searchText = input("\nEnter the Previous Details in ( SUBJECT_NAME : MARKS ) format : ")  #getting the Incorrect SUB-MARKS to be replaced
                replaceText = input("Enter the New Details in ( SUBJECT_NAME : MARKS ) format : ")        #getting the Correct SUB-MARKS to be replaced with
                result = CorrectorFunctions.FieldCorrector(FName, searchText, replaceText)
                
                if(result == True):
                    print("\nSUBJECT MARKS Updated Successfuly.....")
                if(result == False):
                    print("\nSUBJECT MARKS couldn't be Updated.....")

            elif(Cch=="5"):
                result= True

                print("\nENTER THE DETAILS FOR CORRECTION....: ")
                searchText = input("\nEnter the Incorrect Year : ")     #getting the Incorrect YEAR OF PASSING to be replaced
                replaceText = input("Enter the Correct Year : ")        #getting the Correct YEAR OF PASSING to be replaced with
                result = CorrectorFunctions.FieldCorrector(FName, searchText, replaceText)
                
                if(result == True):
                    print("\nYEAR OF PASSINGS Updated Successfuly.....")
                if(result == False):
                    print("\nYEAR OF PASSING couldn't be Updated.....")

            elif(Cch=="6"):            
                    CorrectorFunctions.DateCorrector(FName)
                    print("\nDATE OF ISSUING Updated Successfuly.....")
                

            elif(Cch=="7"):
                result= True

                print("\nENTER THE DETAILS FOR CORRECTION....: ")
                searchText = input("\nEnter the Incorrect Name : ")     #getting the Incorrect NAME of SIGNING AUTHORITY to be replaced
                replaceText = input("Enter the Correct name : ")        #getting the Correct NAME of SIGNING AUTHORITY to be replaced with
                result = CorrectorFunctions.FieldCorrector(FName, searchText, replaceText)
                
                if(result == True):
                    print("\nNAME of SIGNING AUTHORITY Updated Successfuly.....")
                if(result == False):
                    print("\nNAME of SIGNING AUTHORITY couldn't be Updated.....")

            elif(Cch=="0"):
                print( "\nOperation Aborted..............Exiting Module")
                CRunner=False
            else:
                print("INVALID CHOICE.....!!!     CHOOSE AGAIN......")

            #print("\nALL UPDATIONS ACKNOWLEDGED.....")

        except NameError as NE:                                      #exception handeling for NameErrors
            print("\nERROR...!!!", NE, "\n")
        except ValueError as VE:                                     #exception handeling for ValueErrors
            print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
        except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
            print("\nERROR -- NO FILE FOUND ...!!!", FNE, "\n")
            print("\nGoing Back to MAIN MENU.....")
            CRunner= False
        except KeyboardInterrupt:                                    #exception handeling for KeyboardInterrupt 
            print("\n\nINTERRUPTION BY USER  --  OPERATION ABORTED")
        except OSError:                                              #exception handeling for OSError 
            print("ERROR -- Entered Data is NOT VALID")