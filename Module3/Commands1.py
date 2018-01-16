



# # Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print str
#    return;
#
#
# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")



# # Pass by Object Reference
#
# def add(list):
#     list.append('New')
#     print id(list)
#
# list = ['Edureka']
# print id(list)
# add(list)
# print list


# # Variable Scope
# def add(list):
#     list = ['Edureka','New']
#     print id(list)
#
#
# list = ['Edureka']
# print id(list)
# add(list)
# print list


# # id() function and Variable Scope
# def my_multiply(a):
#     print "Before Calculation -> a :: %d, ID :: %d"%(a,id(a))
#     a= a*2
#     print "After Calculation -> a :: %d, ID :: %d" % (a,id(a))
#     return a
#
#
# parameter = 10
# print "Before Function -> parameter :: %d, ID :: %d"%(parameter ,id(parameter))
# parameter = my_multiply(parameter)
# print "After Function -> parameter :: %d, ID :: %d"%(parameter ,id(parameter))
# print parameter



# # Test
#
# def add(list1,list2):
#     list2 = list1
#     list1.append(list2[0])
#
# list1 = ["edureka"]
# list2 = ["python"]
# add(list1,list2)
# print list1
# # print list2


# # Global vs. Local variables
#
# total = 0; # This is global variable.
#
# # Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    global total
#    total = arg1 + arg2; # Here total is local variable.
#    print "Inside the function local total : ", total
#    return total;
#
# # Now you can call sum function
# sum( 10, 20 );
# print "Outside the function global total : ", total



#Function Arguments
    # 1.Required arguments
    # 2.Keyword arguments
    # 3.Default arguments
    # 4.Variable - length arguments

# # 1.Required arguments
# # Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print str
#    return;
#
# # Now you can call printme function
# printme("Hi")


# # 2.Keyword arguments
# # Function definition is here
# def book_my_ticket( fname,lname ):
#    "This prints a passed string into this function"
#    print "Ticket booked for %s %s!"%(fname,lname)
#    return fname;
#
# # Now you can call book_my_ticket function
# book_my_ticket( lname="Potter",fname="Harry")




# # 3.Default arguments
# # Function definition is here
# def book_my_ticket( fname,lname,preference="Any Seat is fine!"):
#    "This prints a passed string into this function"
#    print "Ticket booked for %s %s, Seat Preference : %s seat"%(fname,lname,preference)
#    return;
#
# # Now you can call book_my_ticket function
# book_my_ticket( "Harry","Potter")



# # 4.Variable - length arguments

# # Function definition is here
# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print "Output is: "
#    print "Arg ::%d"%arg1
#    for var in vartuple:
#       print "Var :: %s"%str(var)
#    return;
#
# # Now you can call printinfo function
# #printinfo( 10 )
# printinfo( 70,60,50,80,100,"Test")


# # Anonymous Functions or Lambda Functions
#
# add = lambda arg1, arg2: arg1 + arg2;
# sub = lambda arg1, arg2: arg1 - arg2;
# mul = lambda arg1, arg2: arg1 * arg2;
# div = lambda arg1, arg2: arg1 / arg2;
# mystr = lambda str1: str1.capitalize();
# mylist = lambda list: list[0];
#
#
# # Now you can call sum as a function
# print "Value of total : ", add( 10, 20 )
# print "Value of total : ", sub( 10, 20 )
# print "Value of total : ", mul( 10, 20 )
# print "Value of total : ", div( 10, 20 )
# print mystr("edureka")
# print mylist([70,60,50])

