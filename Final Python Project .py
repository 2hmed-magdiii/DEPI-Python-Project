#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Employee Class
class Employee:
    def __init__(self, id, name, position, salary, email):
        self.id = id
        self.name = name
        self.position = position
        
        if salary < 0:
            raise ValueError(f"Invalid salary: {salary}. Salary must be a positive number.")
        else:
            self.salary = salary
        
        if "@" not in email or "." not in email:
            raise ValueError(f"Invalid email: {email}. Check the email format.")
        self.email = email

    def update_employee_info(self, name=None, position=None, salary=None, email=None):
        if name:
            self.name = name
        if position:
            self.position = position
        if salary is not None:
            if salary < 0:
                raise ValueError(f"Invalid salary: {salary}. Salary must be a positive number.")
            else:
                self.salary = salary
        if email:
            if "@" not in email or "." not in email:
                raise ValueError(f"Invalid email: {email}. Check the email format.")
            else:
                self.email = email

    def display_employee_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}")


# EmployeeManager Class
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, id, name, position, salary, email):
        for emp in self.employees:
            if emp.id == id:
                print("Employee Already Exists.")
                return

        new_employee = Employee(id, name, position, salary, email)
        self.employees.append(new_employee)
        print("Employee Added Successfully.")

    def update_employee(self, id, name=None, position=None, salary=None, email=None):
        for emp in self.employees:
            if emp.id == id:
                emp.update_employee_info(name, position, salary, email)
                print("Employee Updated Successfully.")
                return

        print("Employee Doesn't Exist.")

    def delete_employee(self, id):
        for emp in self.employees:
            if emp.id == id:
                self.employees.remove(emp)
                print("Employee deleted successfully.")
                return

        print("Employee Doesn't Exist.")

    def search_employee(self, id):
        for emp in self.employees:
            if emp.id == id:
                emp.display_employee_info()
                return

        print("Employee Doesn't Exist.")

    def list_all_employees(self):
        if len(self.employees) == 0:
            print("Employees Don't Exist.")
        else:
            for emp in self.employees:
                emp.display_employee_info()


# Program Execution
manager = EmployeeManager()

while True:
    print("\n****************************************************************************")
    print("\n************************ Employee Management System ************************")
    print("\n****************************************************************************")
    
    print("\n\n----------------------------------------------------------------------------")
    print(" 1- Add Employee")
    print("----------------------------------------------------------------------------")
    print(" 2- Update Employee")
    print("----------------------------------------------------------------------------")
    print(" 3- Delete Employee")
    print("----------------------------------------------------------------------------")
    print(" 4- Search Employee")
    print("----------------------------------------------------------------------------")
    print(" 5- List All Employees")
    print("----------------------------------------------------------------------------")
    print(" 6- Exit")
    print("----------------------------------------------------------------------------\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = int(input("Enter Emp ID: "))
        name = input("Enter Emp Name: ")
        position = input("Enter Emp Position: ")
        salary = float(input("Enter Emp Salary: "))
        email = input("Enter Emp Email: ")
        manager.add_employee(id, name, position, salary, email)

    elif choice == "2":
        id = int(input("Enter Emp ID: "))
        name = input("Enter Emp Name: ")
        position = input("Enter Emp Position: ")
        salary = float(input("Enter Emp Salary: "))
        email = input("Enter Emp Email: ")

        manager.update_employee(id, name, position, salary, email)

    elif choice == "3":
        emp_id = int(input("Enter Employee ID to delete: "))
        manager.delete_employee(emp_id)

    elif choice == "4":
        emp_id = int(input("Enter Employee ID to search: "))
        manager.search_employee(emp_id)

    elif choice == "5":
        manager.list_all_employees()

    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice.")


# In[ ]:




