
#Files

# # Open a file
# fo = open("foo.txt", "wb")
# print "Name of the file: ", fo.name
# print "Before Closed: ", fo.closed
# print "Opening mode : ", fo.mode
# print "Softspace flag : ", fo.softspace
#
#
# # Close  file
# fo.close()
# print "After Closed : ", fo.closed





# # Write something to a file
#
# # Open a file
# fo = open("foo.txt", "wb")
# fo.write( "Python is a great language.\nYeah its great!!\n");
#
# # Close opend file
# fo.close()



# Reading from a File

fo = open("foo.txt", "r+")
str = fo.read()
print "Read String is : ", str
# Close opend file
fo.close()

