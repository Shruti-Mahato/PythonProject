# Project
To create an Employee Database using python.
Below are the functions included as part of this project -

### 1. add_employee(emp_id, emp_name, emp_DOJ, emp_designation, emp_salary)
   - Its similar to new onboarding of the employee.
   - Take salary of the employee as default 0.

### 2. add_hr(emp_id, hr_dept, hr_role)
   - hr_dept can be Recruitment, C&B, Admin.
   -  hr_role can be Member, Lead, Manager.

### 3. search_employee(emp_id)
   - Take emp_id as the input to the function.
   - Read the employee file and print the details of the employee.

### 4. search_hr(emp_id)
   - Take emp_id as the input to the function.
   - Read the hr file and print the details of the hr.

> Optional
### 5. Upd_employee(emp_id)
   - Take emp_id as parameter to the function.
   - Display current emp_designation and emp_salary and Prompt for the updated values.
   - Update the record with the new values.

#### > Create a login.txt file with 1 record as below
```plaintext
id - admin
password - admin
```

#### > Create a script for Login module :
Login module should prompt for the followings -
<pre> Welcome to Employee System <br> Please Enter Login id: _____  <br> Please Enter Password: _____  </pre>

#### > Create a script for Admin module :
1.	display menu of choices like below
```plaintext
Welcome Admin!!
     Enter 1 to add employee
     Enter 2 to remove employee
     Enter 3 to add hr
     Enter 4 to remove hr
     Enter q to exit
Enter your Option 
```
###### Following are the operations for different option number-
```plaintext
Option 1: 
	Prompt for emp_id, emp_name, emp_DOJ, emp_designation, emp_salary
	Add a record in “login.txt” with employee_id and Firstname as password
	Add a record in employee file through function already created in Day1
```
```plaintext
Option 2: 
	Prompt for emp_id
	Remove the record “login.txt” for the employee_id
	Remove the record from employee file through function already created in Day1
```
```plaintext
Option 3: 
	Prompt for emp_id
	As Hr is also an employee, first check if the emp_id exist in employee file
	If exist, Prompt for hr_dept, hr_role or else Display error and Quit
	Add a record in hr file through function already created in Day1
```
```plaintext
Option 4: 
	Prompt for emp_id
	Remove the record from hr file through function already created Day1
```
> Optional <br>
>	Update the above programs to generate the emp_id automatically to avoid duplicates


### Create a function for Employee :
1.	If Login_id is NOT of HR, display menu of choices like below -
```plaintext
Welcome <Employee_name>!!
     Enter 1 to view own details
     Enter 2 to view all HR names
     Enter q to exit
Enter your Option
```
For Option 1, Just display all the employee details. <br>
  For Option 2, Display all the Department, HR names, and HR roles (Optional: sorted by Department)

2.	If Login_id is of HR, display menu of choices like below -
```plaintext
Welcome <Employee_name> from HR!!
     Enter 1 to view own details
     Enter 2 to view All employees
     Enter q to exit
Enter your Option
```
For Option 1, Just display all the employee details (Same as Option 1 above and hence should call the same function). <br>
For Option 2, Prompt for Designation, and display details of all the employee with that designation. <br>
if designation is “All”, then display details of all the employees (Optional: sorted by Designation when “All”)
