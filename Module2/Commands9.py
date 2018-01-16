

# # cmp() - This method returns -1 if x < y, returns 0 if x == y and 1 if x > y
#
# print "cmp(80, 100) : ", cmp(80, 100)
# print "cmp(180, 100) : ", cmp(180, 100)
# print "cmp(100, 100) : ", cmp(100, 100)
# print "cmp(80, -100) : ", cmp(80, -100)
#


# #max()
# arr = [2,3,5,7,9,11]
# print "Max value :: %d"%max(arr)
# print "Min value :: %d"%min(arr)

#
# # List to Tuple
# # A tuple is a sequence of immutable Python objects.

arr = [2,3,5,7,9,11]
t = tuple(arr)
print t


# Tuple to List

print list(t)


#Enumerate
enumerate_t = tuple(enumerate(t))
print enumerate_t



# # Xrange is deprecated


