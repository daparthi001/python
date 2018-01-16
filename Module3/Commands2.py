#
def print_friendly_error(e):
    print "Exception Details:"
    print "Error in File ->" + e.filename
    print "Error No ->"+ str(e.errno)
    print "Error String ->" + e.strerror
    print "Error Trace -> " + str(e)

# Errors & Exceptions handling


errorflag = 1

try:
    print "Start doing something..."
    fh = open("testfile.txt", "r")
    fh.write("This is my test file for exception handling!!")
    print "Do something more"

except IOError as e:
    print "Error: can\'t find file or read data"
    errorflag = 1
    print_friendly_error(e)

else:
    print "Written content in the file successfully"

finally:
    print "Finally block executed!"
    if errorflag == 0:
        fh.close()


# Types of Exceptions
# try:
#     i = 1
#     while True:
#         print "This is an infinite loop: " + str(i)
#         i = i+ 1
# except IOError as e:
#     print "\n\n::::::Catch IOError Here::::::"
# # except KeyboardInterrupt as e:
# #     print "\n\n::::::Catch KeyboardInterrupt Here::::::"
# except BaseException as e:
#     print "\n\n::::::Catch Any Exception Here::::::"
#     print_friendly_error(e)
#
# finally:
#     print "\n\nFinally block is executed\n\n"

