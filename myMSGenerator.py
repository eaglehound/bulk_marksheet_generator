# MODULE TO GENERATE MARKSHEETS
# Import date class from datetime module
from datetime import date

#Function to generate the marksheets ( BASIC TEMPLATE )
""" 
Function to Generate the marksheet using the data supplied in Text File containing the bulk data.

-> It has a method MSMaker() : which gets data present in a text file and genrates as many marksheets as the no of Students's data
                                is present in the text file.

"""
try:
    def MSMaker():
        FName = input("\nEnter the File Name with Extension, Conatining Bulk data : ")      #getting the File Name Containing Bulk Data

        SigningAuthority = input("\nEnter the name of signing authority : ")     #getting the name of the Signing authority

        with open(FName, 'r') as DataHandler:   # Opening file conating all details
            c1= DataHandler.read(1)
            c2=int(c1)
            DataHandler.readline()              #To skip 1st line in Bulk data File
            DataHandler.readline()              #To skip 2nd line in Bulk data File

            for y in range(0,c2):
                line = DataHandler.readline()
                data=list(line.split(","))

                MSName =data[0] + data[1] + ".txt"
                    
                with open(MSName, 'w') as MSHandler:
                    #Marksheet Header
                    MSHandler.write("---------------------------------------------------\n")
                    MSHandler.write("------------------   MARKSHEET   ------------------\n")
                    MSHandler.write("---------------------------------------------------\n")

                    # to write "UNIVERSITY of DELHI in centre of marksheet"
                    Header = "UNIVERSITY OF DELHI"
                    x = Header.center(50)
                    MSHandler.write(x + "\n\n")

                    #writing Student's Details
                    MSHandler.write("NAME : " + data[0] + "\n")
                    MSHandler.write("PROGRAMME :" + data[2] + "\n")
                    MSHandler.write("ROLL NO :" + data[1] + "\n\n")

                    #writing SUBJECT MARKS
                    MSHandler.write("SUB1 :" + data[4] + "\n")
                    MSHandler.write("SUB2 :" + data[5] + "\n")
                    MSHandler.write("SUB3 :" + data[6] + "\n")
                    MSHandler.write("SUB4 :" + data[7] + "\n")
                    MSHandler.write("SUB5 :" + data[8] + "\n")

                    MSHandler.write("Year Of Passing : " + data[3] + "\n")

                    today = date.today()        # Returns the current local date

                    MSHandler.write("Date Of Issue : " + str(today) + "\n")
                    MSHandler.write("Signing Authority : " + SigningAuthority + "\n")

                    #Marksheet footer
                    MSHandler.write("---------------------------------------------------\n")
                    MSHandler.write("---------------------------------------------------\n\n\n\n")

except NameError as NE:                                      #exception handeling for NameErrors
    print("\nERROR...!!!", NE, "\n")
except ValueError as VE:                                     #exception handeling for ValueErrors
    print("\nERROR -- INVALID VALUE...!!! : ", VE, "\n")
except FileNotFoundError as FNE:                             #exception handeling for FileNotFoundError
    print("\nNO FILE FOUND ...!!!", FNE, "\n")