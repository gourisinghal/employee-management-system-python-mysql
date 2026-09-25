import os
from colorama import*
from pwinput import*
import pymysql
import time
from tqdm import*
import sys
DB_PASSWORD = input("Enter MySQL password: ")

while True:
    
    os.system("cls")
    os.system("color 1F")
    print("\n"*5)
    
    user=input(Fore.YELLOW+Style.BRIGHT+" "*55+"Enter username:")
    print()
    pas=pwinput(prompt=" "*55+"enter password:",mask='*')
    try:
        con=pymysql.connect(host='localhost',user='root',password='DB_PASSWORD ',database='emp')
        print(""*55+"")
    except Exception as e: 
        print(""*55+"fail",e)

    
    cur=con.cursor()
    q='SELECT * from admin WHERE username=%s and password=%s' 
    val=(user,pas)
    cur.execute(q,val)
    row=cur.fetchone()
    print()
    if (row==None):
        print(Fore.RED+" "*65+"invalid password or username")
        choice=input(Fore.WHITE+" "*65+"try again y/n?")
        if choice in 'yY':
            continue
        elif choice in 'n/N':
            sys.exit()
    else:
        break

#splash screen page coding 
os.system("cls")
os.system("color 0A")
print("\n"*3)
print(Fore.BLUE+Style.BRIGHT+" "*65+"E M P L O Y E E  M A N A G E M E N T  ")
print()
print(Fore.BLUE+" "*75+"S Y S T E M")
print("\n"*3)
print(Fore.CYAN+" "*77+"version 1.0")
print()
print(Fore.WHITE+" "*73+"DEVELOPED BY DB_PASSWORD  ")
print("\n"*4)
print(Fore.GREEN)
for i in tqdm(range (5),desc="please wait"):
    time.sleep(0.3)
print(Fore.WHITE)
os.system("pause")



#add employee page coding

def add_employee():
    
    os.system("cls")
    
    print(Fore.YELLOW+"Add Employee Record")
    print("----------------------------------------------")
    try:
        empid = int(input(Fore.YELLOW + "employee id :"))
    except ValueError:
        print("\n")
        print(Fore.RED+"Please enter numbers only integer")
        
        os.system('pause')
        main_menu()
    
    name=input(Fore.YELLOW+"enter name:")
    email=input("enter email:")

    try:
        phone = int(input(Fore.YELLOW + "enter phone number:"))
    except ValueError:
        print("\n")
        print(Fore.RED+"something is wrong with phone number..")
        os.system('pause')
        main_menu()
    
    address=input("enter address:")
    post=input("enter post:")
    try:
        salary = int(input(Fore.YELLOW + "enter salary :"))
    except ValueError:
        print("\n")
        print(Fore.RED+"Please enter numbers only integer")
        os.system('pause')
        main_menu()
    
    con=pymysql.connect(host='localhost', user='root',password ='DB_PASSWORD ',database='emp',autocommit=True)
    cur=con.cursor()
    q="INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val=(empid,name,email,phone,address,post,salary)
    cur.execute(q,val)
    print(Fore.GREEN+"Data saved sucessfully")
    os.system('pause')
    main_menu()


#delete employee page coding
def delete_employee():
    os.system("cls")
    print(Fore.GREEN+"DELETE EMPLOYEE RECORD")
    print("----------------------------------------------")
    empid=int(input(Fore.YELLOW+"enter employee id: "))
    print()
    print(Fore.WHITE+"Employee Record")
    print("-----------------------------------------------")
    con=pymysql.connect(host="localhost",user="root",password="DB_PASSWORD ",database="emp",autocommit=True)
    cur=con.cursor()
    q="SELECT*FROM employee where id=%s"
    val=(empid,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print(Fore.RED+"Not Found")
    else:
        print(Fore.WHITE+"Employee record")
        print("---------------------------------")
        print("employee id:",row[0])
        print("employee name:",row[1])
        print("employee email",row[2])
        print("employee phone",row[3])
        print("employee address",row[4])
        print("employee post",row[5])
        print("employee salary",row[6])
        print("----------------------------------------")
        choice=input("Do you want to delete Y/N?")
        if choice in "y/Y":
            q="DELETE FROM employee WHERE id=%s"
            cur.execute(q,val)
            print()
    print(Fore.GREEN+"successfully deleted")
        
    os.system("pause")
    main_menu()

#search emplyee
def search_employee():
    os.system("cls")
    print(Fore.GREEN+"search employee:")
    print("----------------------------------------")
    empid=int(input(Fore.YELLOW+"enter employee id:"))
    print()
    con=pymysql.connect(host='localhost',user='root',password='DB_PASSWORD ',database='emp',autocommit=True)
    cur=con.cursor()
    q="SELECT*FROM employee WHERE id=%s"
    val=(empid,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print(Fore.RED+"NOT FOUND")
    else:
        print(Fore.WHITE+"Employee record")
        print("---------------------------------")
        print("employee id:",row[0])
        print("employee name:",row[1])
        print("employee email",row[2])
        print("employee phone",row[3])
        print("employee address",row[4])
        print("employee post",row[5])
        print("employee salary",row[6])
    os.system("pause")
    main_menu()

#edit employee page coding
def edit_employee():
    os.system('cls')
    print(Fore.GREEN+"EDIT EMPLOYEE RECORD")
    print('------------------------------------')
    empid=int(input(Fore.YELLOW+"Enter employee id:"))
    con=pymysql.connect(host="localhost",user='root',password='DB_PASSWORD ',database='emp',autocommit=True)
    cur=con.cursor()
    q='SELECT * FROM employee WHERE id=%s'
    val=(empid,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print()
        print(Fore.RED+"NOT FOUND")
    else:
        print()
        print(Fore.WHITE+"employee record")
        print('---------------------------')
        print("employee id:",row[0])
        print("name:",row[1])
        print("Email:",row[2])
        print("phone:",row[3])
        print("Address:",row[4])
        print("post:",row[5])
        print("salary:",row[6])
        print("-----------------------------")
        choice=input(Fore.YELLOW+"do u want to edit y/n?")
        print()
        if choice in "yY":
            name=input("enter name:")
            email=input("enter email:")
            phone=input("enter phone:")
            address=input("enter address:")
            post=input("enter post:")
            salary=input("enter salary:")
            con=pymysql.connect(host='localhost',user='root',password='DB_PASSWORD ',database='emp',autocommit=True)
            cur=con.cursor()
            q="UPDATE employee SET name=%s,email=%s,phone=%s,address=%s,post=%s,salary=%s WHERE id=%s"
            val=(name,email,phone,address,post,salary,empid)
            cur.execute(q,val)
            print()
            print(Fore.GREEN+"SUCESSFULLY UPDATED")
    os.system('pause')
    main_menu()

#list of employees page coding
def list_emp():
    os.system('cls')
    print()
    print(" "*55+'LIST OF EMPLOYEES')
    print()
    print('='*172)

    print('%10s %15s %25s %29s %25s %25s %25s'%('ID','NAME','EMAIL','PHONE','ADDRESS','POST','SALARY'))

    print('='*172)
    con=pymysql.connect(host='localhost',user='root',password='DB_PASSWORD ',database='emp',autocommit=True)
    cur=con.cursor()
    q='SELECT * FROM employee '
    cur.execute(q)
    rows=cur.fetchall()
    for row in rows:
        print('%10s %15s %25s %29s %25s %25s %25s'%(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    os.system('pause')
    main_menu()

#promote employee page
def promote_employee():
    os.system("cls")
    print(Fore.GREEN+"PROMOTE EMPLOYEE")
    print("-----------------------------------")
    empid=int(input(Fore.WHITE+"Enter employee id:"))
    con=pymysql.connect(host='localhost',user='root',password='DB_PASSWORD ',database='emp',autocommit=True)
    cur=con.cursor()
    q='SELECT * FROM employee WHERE id=%s'
    val=(empid,)
    cur.execute(q,val)
    row=cur.fetchone()
    print()
    newsalary=int(input(Fore.YELLOW+"enter new salary:"))
    if (newsalary==row[6]):
        print(Fore.RED+"New Salary is equal to current salary \n\npromote unsuccesful")
        
    elif(newsalary<row[6]):
        print(Fore.RED+"New Salary is less than current salary\n\npromote unsuccesful")
    elif(newsalary>row[6]):
        q='UPDATE employee SET salary=%s WHERE id=%s'
        val=(newsalary,empid)
        cur.execute(q,val)
        print()
        print(Fore.GREEN+"Promoted successfully")
    os.system('pause')
    main_menu()

#change passsword page
def change_password():
    os.system('cls')
    print(Fore.GREEN+" "*75+"CHANGE PASSWORD")
    print("="*172)
    print("\n"*5)
    currpass=input(Fore.YELLOW+" "*70+"Enter password:")
    print()
    con=pymysql.connect(host='localhost',user='root',password='DB_PASSWORD ',database='emp',autocommit=True)
    cur=con.cursor()
    q="SELECT * FROM admin WHERE password=%s"
    val=(currpass,)
    cur.execute(q,val)
    row=cur.fetchone()
    if row==None:
        print()
        print(Fore.RED+" "*70+"incorrect password")
        choice=input(Fore.WHITE+" "*70+"Try Again Y/N?")
        if choice in "yY":
            change_password()
    else:
        newpass=input(Fore.WHITE+" "*70+"Enter new password:")
        conpass=input(Fore.WHITE+" "*70+"Enter confirm password:")
        if newpass!=conpass:
            print(Fore.RED+" "*70+"Password missmatched")
            choice=input(Fore.WHITE+" "*70+"Try again y/n?")
            if choice in "Yy":
                change_password()
        else:
            q="UPDATE admin SET password=%s"
            val=(newpass,)
            cur.execute(q,val)
            print(Fore.GREEN+" "*70+"Successfully Updated")
    os.system("pause")
    main_menu()

    

#menu page coding
def main_menu():
    print('\n')
    os.system('cls')
    print("\n"*2)
    print(Fore.GREEN+Style.BRIGHT+" "*70+"M A I N   M E N U")
    print(" "*55+"------------------------------------------")
    print(Fore.WHITE+" "*55+ "  1. Add Employee Details")
    print()
    print(" "*55+ "  2. Delete Employee Details")
    print()
    print(" "*55+ "  3. Search Employee Details")
    print()
    print(" "*55+ "  4. Edit Employee Details")
    print()
    print(" "*55+ "  5. list of Employee Details")
    print()
    print(" "*55+ "  6. promote Employee ")
    print()
    print(" "*55+ "  7. change password")
    print()
    print(" "*55+ "  8. exit")
    print(Fore.GREEN+" "*55+"-------------------------------------------------")
    try:
        choice = int(input(Fore.YELLOW + Style.BRIGHT + " "*67 + "enter your choice? :"))
    except ValueError:
        print("\n")
        print(" "*67+"Please enter numbers only (1-8)")
        return

  
    if choice==1:
        add_employee()
    elif choice==2:
        delete_employee()

    elif choice==3:
        search_employee()
    
    elif choice==4:
        edit_employee()

    elif choice==5:
        list_emp()
    elif choice==6:
        promote_employee()
    elif choice==7:
        change_password()
    elif choice==8:
        os.system('cls')
        print (Fore.GREEN+" "*70+"Project Terminated")
        sys.exit()
    else:
        print(Fore.RED+" "*70+"Invalid choice")
        
        


        

main_menu()



   

