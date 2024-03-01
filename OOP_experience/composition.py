

class Salary:
    def __init__(self, payment, bonus):
        self.payment = payment
        self.bonus = bonus

    def annual_salary(self):
        return (self.payment * 12) + self.bonus


class Employee:
    def __init__(self, name, age, payment, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(payment, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()


emp = Employee('Tetiana', 25, 35000, 12000)
print(emp.total_salary())
