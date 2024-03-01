import datetime


class Employee:

    num_of_empls = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_empls += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# add employees
emp_1 = Employee("Tetiana", "Kucherenko", 25000)
emp_2 = Employee("Kate", "Wilson", 45000)

emp_3 = "John-Doe-7000"
new_emp = Employee.from_string(emp_3)

# raise payment
Employee.set_raise_amt(1.05)

# check if it is a working day
my_date = datetime.date(2022, 2, 7)
print(Employee.is_workday(my_date))
