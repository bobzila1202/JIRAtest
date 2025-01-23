class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname,lname)
        self.salary = salary
        
    def calculate_paycheck(self):
        return self.salary/52
    def display_employee(self):
        print(self.fname)
        
class ComissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    
    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_num*self.com_rate
        return regular_salary+total_commission
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
        
    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate
    

class Company:
    def __init__(self):
        self.employees = []
        
    def add_employees(self, new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print("Current employees:")
        for i in self.employees:
            print(i.fname, i.lname)
        print("-----------")
        
    def pay_employees(self):
        print("Paying employees:")
        for i in self.employees:
            print("Paycheck for", i.fname, i.lname)
            print("Amount:", i.calculate_paycheck())
            print("---------------------")
        
def main():
    my_company = Company()
    
    employee1 = SalaryEmployee("Sarah", "Hess", 50000)
    my_company.add_employees(employee1)
    employee2 = HourlyEmployee("bob", "Hess", 25, 50)
    my_company.add_employees(employee2)
    employee3 = ComissionEmployee("tim", "Hess", 30000, 5, 200)
    my_company.add_employees(employee3)
    
    my_company.display_employees()
    my_company.pay_employees()
    
    
main()
    