# # Inheritance
#
# class Chart:        # define parent class
#
#     parentAttr = "This is a dummy chart title" # Class variable
#
#     def __init__(self):
#         print "Calling Chart constructor"
#
#     def parentMethod(self):
#         print 'This is Parent Chart Class Method'
#
#     def set_chart_title(self, attr):
#         Chart.parentAttr = attr
#
#     def get_chart_title(self):
#         print "Parent attribute :", Chart.parentAttr
#
#     def show_chart_labels(self):
#         print "Showing Base chart Labels"
#
# class PieChart(Chart): # define child class
#
#     def __init__(self):
#         print "Calling PieChart constructor"
#
#     def load_some_data(self):
#         print 'Calling child method'
#
#     def show_chart_labels(self):
#         print "Showing Pie chart Labels"
#
#
# c = PieChart()          # instance of child
# c.load_some_data()      # child calls its method
# c.parentMethod()        # calls parent's method
# c.set_chart_title("This is my first chart")       # again call parent's method
# c.get_chart_title()          # again call parent's method
# #
# # #Overriding Methods - Polymorphism
# c.show_chart_labels()
#


#Overloading Operators
# #
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print v1 + v2
#



#


# # Private Members of a Class
#
# class JustCounter:
#     __secretCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         print self.__secretCount
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print counter.__secretCount




# Example

class edureka:
    def __init__(self):
        self.__pri = "I am Private"
        self._pro = "I am Protected"
        self.pub = "I am Public"

    def update_my_pri_variable(self,str):
        if len(str) > 5:
            self.__pri = str

    def print_my_private_variable(self):
        print self.__pri

obj = edureka()

# print obj.pub
# obj.pub = "I can be Updated"
# print obj.pub


# print obj._pro
# obj._pro = "I can be Updated"
# print obj._pro
#



#
# obj.print_my_private_variable()
# obj.update_my_pri_variable("abcdef")
# obj.print_my_private_variable()



