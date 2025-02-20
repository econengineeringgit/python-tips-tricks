class Employee:
    
    general_raise = 1.15

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@econengineering.com'
        self.pay = pay

    
    def apply_raise(self):
        self.pay = int(self.pay * 1.15)
        # self.pay = int(self.pay * self.general_raise)
        # self.pay = int(self.pay * Employee.general_raise)
        
        
emp_1 = Employee('Jakab', 'Gipsz', 300)
emp_2 = Employee('Test', 'Employee', 200)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


###


# # Access class variable
# print(emp_1.general_raise)
# print(emp_2.general_raise)
# print(Employee.general_raise)

print(emp_1.__dict__)
print(Employee.__dict__)


###

emp_1.general_raise = 1.2

print(emp_1.general_raise)
print(emp_2.general_raise)
print(Employee.general_raise)
