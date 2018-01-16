# class Employee:
#     """An Employee of XYZ Company. Employee class has the
#     following properties:
#
#     Attributes:
#         name: A string representing the name.
#         balance: A float tracking the current balance of the account.
#     """
#
#     def __init__(self, name,balance=0.0):
#         """Return a Customer object whose name is *name*."""
#         self.name = name
#         self.balance = balance
#
#     def set_balance(self, balance=0.0):
#         """Set the customer's starting balance."""
#         self.balance = balance
#
#     def withdraw(self, amount):
#         """Return the balance remaining after withdrawing *amount*
#         dollars."""
#         if amount > self.balance:
#             raise RuntimeError('Amount greater than available balance.')
#         self.balance -= amount
#         return self.balance
#
#     def deposit(self, amount):
#         """Return the balance remaining after depositing *amount*
#         dollars."""
#         self.balance += amount
#         return self.balance
#
# obj = Employee("User1")
# obj.deposit(10000)



# #Static methods
#
# class Car:
#     'This is a class for car'
#
#     def make_car_sound(self):
#         print "VRooooommmm!"
#
# c = Car()
# c.make_car_sound()
#
# class Car:
#     ''
#     @staticmethod
#     def make_car_sound():
#         print "sd sd sdVRooooommmm!"
#
# Car.make_car_sound()


#

# # Class Attributes
#
# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print "Name : ", self.name, ", Salary: ", self.salary


# # "This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# # "This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount


# print hasattr(emp1,'age')
# emp1.age = 7
# print emp1.age
# print hasattr(emp1,'age')
# emp1.age = 8
# print emp1.age
# del emp1.age
# print hasattr(emp1,'age')



# print hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
# print setattr(emp1, 'age', 8) # Set attribute 'age' at 8
# print getattr(emp1, 'age')    # Returns value of 'age' attribute
# delattr(emp1, 'age')    # Delete attribute 'age'
# print hasattr(emp1, 'age')
#

# # Default Class Attributes
# print Employee.__dict__
# print Employee.__doc__
# print Employee.__name__
# print Employee.__module__
# print Employee.__bases__




# # __del__
# class Point:
#     def __init__( self, x=0, y=0):
#       self.x = x
#       self.y = y
#
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print class_name, "destroyed - This is my destructor"
#
# pt1 = Point()
# pt2 = pt1
# pt3 = Point(10,10)
# print "ID of pt1 :: %s"%str(id(pt1))
# print "ID of pt2 :: %s"%str(id(pt2))
# print "ID of pt3 :: %s"%str(id(pt3))
# del pt1
# del pt2
# del pt3
