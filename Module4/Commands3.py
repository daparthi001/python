
# Simple Class in Python

class Employee:
    'Common base class for all employees'
    empCount = 0

    #Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary



print Employee.__doc__

tom = Employee("Tom Hanks","$1 Million")
tom.displayCount()
tom.displayEmployee()
print Employee.empCount

edu = Employee("Edureka User","$100 Million")
edu.displayCount()
edu.displayEmployee()

print Employee.empCount
