def display():
        with open('emp_database.txt','r') as emp:
            for line in emp:
                lst=line.strip().split('|')
                print("\nEmployee id : {}\nName : {}\nDate of joining : {}\nDesignation : {}\nSalary : {}\n".format(lst[0],lst[1],lst[2],lst[3],lst[4]))

def emp_login(id):
    def hr_deatils():
        with open('hr.txt','r') as hr:
            for line in hr:
                lst2 =line.strip().split('|')
                with open('emp_database.txt','r') as emp:
                    for line in emp:
                        lst=line.strip().split("|")
                        if(lst[0]==lst2[0]):
                            break
                print("\nHR department : {}\nHR name : {}\nHR role : {}\n".format(lst2[1],lst[1].upper(),lst2[2]))
        
    while True:
         with open('emp_database.txt','r') as emp:
            for line in emp:
                lst=line.strip().split("|")
                if(lst[0]==id):
                    break
            print('Welcome {} !!'.format(lst[1].upper()))
            print("\nEnter 1 to view own details.\nEnter 2 to view all HR names\nEnter q to exit.\n")
            choice = input("Enter your Choice: ")
            if choice == '1':
                display()
            elif choice == '2':
                hr_deatils()
                
            elif choice == 'q':
                break
            else:
                print('Invalid input')
                
def hr_login(id):
    
    def dis_desig(des):
        with open('emp_database.txt','r') as emp:
            for line in emp:
                lst=line.strip().split('|')
                if(lst[3]==des):
                    print("\nEmployee id : {}\nName : {}\nDate of joining : {}\nDesignation : {}\nSalary : {}\n".format(lst[0],lst[1],lst[2],lst[3],lst[4]))
    while True:
         with open('emp_database.txt','r') as emp:
            for line in emp:
                lst=line.strip().split("|")
                if(lst[0]==id):
                    break
            print('Welcome {} from HR !!'.format(lst[1].upper()))
            print("\nEnter 1 to view own details.\nEnter 2 to view all employees\nEnter q to exit.\n")
            choice = input("Enter your Choice: ")
            if choice == '1':
                display()
                
            elif choice == '2':
                des=input("Enter the designation : ")
                if des=='All':
                    display()
                else:
                    dis_desig(des)
                
            elif choice == 'q':
                break
                
            else:
                print('Inavlid input')