# creating a class

class Employee:

    # defining a parameterized constructor( here self is nothing but "this" in java)

    def __init__(self, emp_name, emp_id, emp_position, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_position = emp_position
        self.emp_salary = emp_salary
        self.emp_leave = 15

    # creating a method, here self is the default parameter

    def update_leaves(self,leaves_taken):
        return f"Your available leave balance is {self.emp_leave-leaves_taken}"

    # This is method will be called when we call print
    def __str__(self):
        return (f"Employee name is {self.emp_name}, his Employee id is {self.emp_id}, "
                f"his position in the organization is {self.emp_position}, his salary is {self.emp_salary} and he has {self.emp_leave} leave balance  ")

# creating an employee object

emp_object = Employee("Soniya",123456,"Software Engineer","GBP 50000 PA")

# printing employee object

print(f"{emp_object}")

# calling the function

off_days = int(input("Please enter no.of days leave taken "))
result = emp_object.update_leaves(off_days)
print(result)
