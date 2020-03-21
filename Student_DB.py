#Dylan DeWolfe
#dewol103@mail.chapman.edu
#CPSC 408
# Assignment 2 SQLite CRUD Application


import sqlite3
import pandas as pd
from pandas import DataFrame
from Student import Student

#-----------------------------------------------------------------------------------------------------------
## Connections
conn = sqlite3.connect('C:/Users/dylan/OneDrive/Desktop/Assignment2/StudentDB.sqlite')
c = conn.cursor() ## allows python to execute sql statement
#-----------------------------------------------------------------------------------------------------------
## Creating Object of Student Class
#stu = Student('7999994','Dylan','DeWolfe','Nonsense','3.0','Spongebob','FALSE')
#-----------------------------------------------------------------------------------------------------------
## Testing Database
#sql_command = "INSERT INTO Student('FirstName','LastName','Major','GPA','FacultyAdvisor','IsDeleted') VALUES ('Rene', 'German', 'CS');"
#c.execute(sql_command)
#-----------------------------------------------------------------------------------------------------------

## Inserting Object of Student Class
#sql_command2 = "INSERT INTO Student('StudentId','FirstName','LastName','Major','GPA','FacultyAdvisor','IsDeleted') VALUES (?,?,?,?,?,?,?);"

#c.execute(sql_command2,(stu.getStudent()))
#--------------------------------------------------------------------------------------------------------------
## Update
## updates major to comm based on studentID, in this case where student ID = 11
#c.execute("Update Student SET Major = ? WHERE StudentId = ?", ('COMM',11))
#--------------------------------------------------------------------------------------------------------------
#conn.commit()
studentId = c.lastrowid
#print("Record Created", studentId)
#print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#--------------------------------------------------------------------------------------------------------------
## Display Menu Function
def Menu():
    ans=True
    while ans:
        print("""
        1.Display Students
        ----------------------
        2.Create a Student
        ----------------------
        3.Update Student Record
        ----------------------
        4.Delete Student
        ----------------------
        5. Search Student by Major, GPA, or Advisor
        ----------------------
        6. Exit 
        ----------------------
        """)
        ans= input("What operation would you like to perform (choose by #): ")
        if ans=="1":
            Display()
        elif ans=="2":
            addStudent()
        elif ans=="3":
            updateStudent()
        elif ans=="4":
            deleteStudent()
        elif ans=="5":
            searchStudent()
        elif ans=="6":
            break
        else:
            print("\n Not Valid, Try again!!!!!!!!")


#--------------------------------------------------------------------------------------------------------------
## user input for creating a student // prob should turn into a function later
def addStudent():
    print("Enter the Student' Id #: ")
    userin_id =input()
    print("Enter the Student's First Name: ")
    userin_Fname =input()
    print("Enter the Student's Last Name: ")
    userin_Lname =input()
    print("Enter the Student's Major: ")
    userin_Major =input()
    print("Enter the Student's GPA: ")
    userin_GPA =input()
    print("Enter the Student's Facutly Advisor: ")
    userin_fAdvis =input()

    input_student = Student(userin_id,userin_Fname,userin_Lname,userin_Major,userin_GPA,userin_fAdvis,'FALSE')

    #print(input_student.getStudent()) // testing user inputted values

    sql_command3 = "INSERT INTO Student('StudentId','FirstName','LastName','Major','GPA','FacultyAdvisor','IsDeleted') VALUES (?,?,?,?,?,?,?);"
    c.execute(sql_command3,(input_student.getStudent()))
    studentId = c.lastrowid
    conn.commit()
    print("Record Created", studentId)
    ## End Adding entry by user code
#--------------------------------------------------------------------------------------------------------------
## Delete Works
def deleteStudent():
    print("Enter the Student ID of the Student that you would like to Delete: ")
    delete_Student = input()
    #Update the entry with the ID and set the BOOL to TRUE
    ## added [] to fix binding issues...
    c.execute("UPDATE Student SET IsDeleted = 'TRUE' WHERE isDeleted = 'FALSE' AND StudentId = ?;",[delete_Student])
    #c.execute(sql_delete)
    conn.commit()
    print("Deleted Student: " + delete_Student)

#--------------------------------------------------------------------------------------------------------------
def updateStudent():
## Simple Update from screenshots

    print("Would you like to update a Student's Major, Advisor, or Both?:")
    print("""
            1.Update Student's Major
            ----------------------
            2.Update Student's Faculty Advisor
            ----------------------
            """)
    u_choose = input()
    if u_choose == "1":
        print("Enter the Student's ID #: ")
        user_updateid = input()
        print("Enter the *new Major: ")
        user_updateTO = input()
        c.execute("UPDATE Student SET MAJOR = ? WHERE StudentId = ?;",[user_updateTO,user_updateid])
        conn.commit()
    elif u_choose == "2":
        print("Enter the Student's ID #: ")
        user_updateid = input()
        print("Enter the *new Faculty Advisor: ")
        user_updateTO = input()
        c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?;", [user_updateTO, user_updateid])
        conn.commit()
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
def searchStudent():
    print("Would You Like To Search by Major, GPA, or Advisor? ")
    print("""
                1.Search and Display by Major
                ----------------------
                2.Search and Display by GPA
                ----------------------
                3.Search and Display by Advisor
                ----------------------
                """)
    u_choose = input()
    if u_choose == "1":
        print("Enter the Major: ")
        major_in = input()
        c.execute("SELECT * FROM Student WHERE Major IS ? AND isDeleted IS 'FALSE';", [major_in])
        conn.commit()
        all_rows = c.fetchall()
        df = DataFrame(all_rows,columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'IsDeleted'])
        print(df)

    elif u_choose == "2":
        print("Enter the GPA: ")
        gpa_in = input()
        c.execute("SELECT * FROM Student WHERE GPA IS ? AND isDeleted IS 'FALSE';", [gpa_in])
        conn.commit()
        all_rows = c.fetchall()
        df = DataFrame(all_rows,
                       columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'IsDeleted'])
        print(df)
    elif u_choose == "3":
        print("Enter the Advisors Name: ")
        advisor_in = input()
        c.execute("SELECT * FROM Student WHERE FacultyAdvisor IS ? AND isDeleted IS 'FALSE';", [advisor_in])
        conn.commit()
        all_rows = c.fetchall()
        df = DataFrame(all_rows,
                       columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'IsDeleted'])
        print(df)
#--------------------------------------------------------------------------------------------------------------
## Display All Students
def Display():
    c.execute("SELECT * FROM Student WHERE IsDeleted IS 'FALSE' ")
    all_rows = c.fetchall()
    df = DataFrame(all_rows, columns= ['StudentId','FirstName','LastName','GPA','Major','FacultyAdvisor','IsDeleted'])
    print(df)

#for x in all_rows:
#    print(x)
##-------------------------------------------------------------------------------------------------------------
## Testing Functions
Menu()
#addStudent()
#Display()

