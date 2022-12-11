class Employee:
      def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Developer(Employee):
  def __init__(self, name, salary, skills):
    super().__init__(name, salary)
    self.skills = skills


class Tester(Employee):
  def __init__(self, name, salary, experience):
    super().__init__(name, salary)
    self.experience = experience


class Manager(Employee):
  def __init__(self, name, salary, employees=None):
    super().__init__(name, salary)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_employee(self, employee):
    self.employees.append(employee)

  def remove_employee(self, employee):
    self.employees.remove(employee)

  def display_employees(self):
    for employee in self.employees:
      print(f"{employee.name} ({type(employee).__name__})")

# Test the classes
dev1 = Developer("John", 10000, ["Java", "Python"])
dev2 = Developer("Jane", 12000, ["JavaScript", "C++"])
tester1 = Tester("Mike", 9000, 2)
tester2 = Tester("Emily", 8500, 3)
manager = Manager("Sam", 15000, [dev1, tester1])

manager.add_employee(dev2)
manager.add_employee(tester2)
manager.display_employees()
