def add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary):
    with open('emp_database.txt','a') as e:
        e.write('{}|{}|{}|{}|{}\n'.format(emp_id,emp_name,emp_DOJ,emp_designation,emp_salary))
    with open('login.txt', 'a') as l:
        name = emp_name.split()
        l.write('{} {}\n'.format(emp_id,name[0]))
    return "\nEmployee added Successfully !!\n"


def remove(emp_id, files, s):
    f = open(files, 'r')
    a = f.readlines()
    for i in range(len(a)):
        j = a[i].split(s)
        if j[0] == emp_id:
            a[i] = ''
            break
    f.close()
    f = open(files, 'w')
    f.writelines(a)
    f.close()

def remove_employee(emp_id):
    remove(emp_id, 'emp_database.txt', '|')
    remove(emp_id, 'hr.txt', '|')
    remove(emp_id, 'login.txt', ' ')
    
    
def check(emp_id):
    flag = False
    with open("emp_database.txt", 'r') as emp:
        for i in emp.readlines():
            j = i.split('|')
            if j[0] == emp_id:
                flag = True
    return flag


def add_hr(emp_id, hr_dept, hr_role):
    with open('hr.txt','a') as h:
         h.write('{}|{}|{}\n'.format(emp_id,hr_dept,hr_role))
    return "\nHR added successfully !!\n"


def remove_hr(emp_id):
    remove(emp_id, 'hr.txt', '|')


while True:
    print("\nWelcome to admin!!")
    print("1. to add employee\n2. to remove employee\n3. to add hr\n4. to remove hr\n5.Enter q to exit\n")
    choice = input("Enter your Choice: ")
    if choice == '1':
        emp_name = input("Employee Name : ")
        emp_DOJ = input("Date of Joining : ")
        emp_designation = input("Designation: ")
        emp_salary = float(input("Salary : "))
        with open('emp_database.txt','r') as e:
            i=0
            for line in e:
                lst=line.strip().split('|')
                i=int(lst[0])
        emp_id=i+1
        print(emp_id)
        print(add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary))
        
    elif choice == '2':
        emp_id = input("Enter the Employee ID to remove : ")
        if(check(emp_id)):
            remove_employee(emp_id)
        else:
            print("Employee does not exist.")
            
    elif  choice == '3':
        emp_id = input("Enter the Employee ID : ")
        if (check(emp_id)):
            hr_dept = input("HR Department - ")
            hr_role = input("HR Role ")
            print(add_hr(emp_id, hr_dept, hr_role))
        else:
            print("Employee does not exist.")
            
    elif choice == '4':
        emp_id = input("Enter the Employee ID : ")
        if (check(emp_id)):
            remove_hr(emp_id)
        else:
            print("Employee id doesn't exist.")
            
    elif choice == 'q':
        break
    else:
        print('Inavlid input')