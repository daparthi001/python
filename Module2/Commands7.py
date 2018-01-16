# Lists

# # empty list
# my_list = []
# print my_list
#
# # list of integers
# my_list = [1, 2, 3]
# print my_list


# # list with mixed datatypes
# my_list = [1, "Hello", 3.4]
# print my_list



# # nested list
# my_list = ["mouse", [8, 4, 6], ['a']]
# print my_list



#
# my_list = ['e','d','u','r','e','k','a']
# # # Output: e
# print my_list[0]
#
# # Output: d
# print my_list[2]
#
# # Output: e
# print my_list[5]
# #
# # # Error! Only integer can be used for indexing
# # my_list[4.0]
#
#





# Nested List
# n_list = ["Happy", ['e','d','u','r','e','k','a'], True]

# Nested indexing

# # Output: a
# print n_list[0][0]
# print n_list[0]
# print n_list[0][3:]

#
# # Output: 5
# print n_list[1][3]
# print n_list[1][3:]
# print n_list[1][:1]
# print n_list[1][2:5]




#Negative Indexing


# my_list = ['e','d','u','r','e','k','a']
#
# # Output: a
# print my_list[-1]
# print my_list[-2]
# print my_list[-3]



# List Slicing

#
# my_list = ['e','d','u','r','e','k','a']
#
# print "elements 3rd to 5th"
# print my_list[2:5]
#
# print "elements beginning to 4th"
# print my_list[:-5]
#
# print "elements upto to 4th"
# print my_list[:5]
#
# print "elements 6th to end"
# print my_list[5:]
#
# print "elements beginning to end"
# print my_list[:]









# #Add elements to a list
#
# # mistake values
# odd = [2, 4, 6, 8]
# print odd[:]
#
# # change the 1st item
# odd[0] = 1
#
# # Output: [1, 4, 6, 8]
# print odd
#
# # change 2nd to 4th items
# odd[1:4] = [3, 5, 7]
#
# # # Output: [1, 3, 5, 7]
# print odd


# #Append to List
#
# #
# odd = [1, 3, 5]
#
# odd.append(7)
#
# # Output: [1, 3, 5, 7]
# print odd
#
# odd.extend([9, 11, 13])
#
# # Output: [1, 3, 5, 7, 9, 11, 13]
# print odd
#


# #Using '+' operator on List
#
# odd = [1, 3, 5]
#
# # Output: [1, 3, 5, 9, 7, 5]
# print odd + [9, 7, 5]

# #Output: ["re", "re", "re"]
# print ["re"] * 3
# print [7]*50










# # #Insert to List
# #
# odd = [1, 9]
# # odd.insert(0,3)
# #
# # # Output: [1, 3, 9]
# # print odd
#
# odd[2:2] = [5, 7]
#
# # Output: [1, 3, 5, 7, 9]
# print odd




# #Delete from a List
# #
#
# my_list = ['e','d','u','r','e','k','a']
#
# # delete one item
# del my_list[2]
# #
# # # Output: ['e','d','u','r','e','k','a']
# print my_list
# #
# # delete multiple items
# del my_list[1:5]
# #
# print my_list
# #
# # delete entire list
# del my_list
#
# # Error: List not defined
# print my_list
#








#
# List Manipulation

my_list = ['e','d','u','r','e','k','a']

# my_list.remove('p')

# my_list.remove('k')

# print my_list
# print my_list.pop(1)
# print my_list
# print my_list.pop()
# print my_list

#my_list.clear()

# Output: []
#print my_list
#


#
# #List Index
# my_list = [3, 8, 1, 6, 0, 8, 4]
#
# # # Output: 1
# print "Index of 8 is :: %d"%my_list.index(8)
# #
# # Output: 2
# print my_list.count(8)
# #
# my_list.sort()
#
# #
# # # Output: [0, 1, 3, 4, 6, 8, 8]
# print my_list
# #
# print "Index of 8 is :: %d"% my_list.index(8)
#
#
# my_list.reverse()
#
# # Output: [8, 8, 6, 4, 3, 1, 0]
# print my_list
#


#
# my_list = [8, 8, 6, 4, 3, 1, 0]
#
# if 99 not in my_list:
#     print "Item is not present"

