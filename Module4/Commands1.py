
#Regular Expressions

import re

#Common usage
# String Search & String Manipulation


# RE Methods
# 1- re.match()
# 2- re.search()
# 3- re.findall()
# 4- re.split()
# 5- re.sub()
# 6- re.compile()

#
# # 1- re.match() - only matches string at beginning of string
# result = re.match('Python', 'Python is a good language to learn')
# print result
# print result.start()
# print result.end()


# # 2- re.search() Finds match anywhere in the string
#
# result = re.search('good', 'Python is a good language to learn')
# print result.group()
# print result.start()
# print result.end()

# # 3- re.findall() - Get a list of all matching patterns
#
# result = re.findall('Python', 'Python is a good language to learn. I like learning Python. Python rocks.')
# print result



# # 4- re.split() - Split a string by a pattern
# result = re.split(';', 'abcd;efgh;ijkl')
# print result
# result = re.split(';', 'abcd;efgh;ijkl',maxsplit=1)
# print result



# 5- re.sub() - Substitute a string with a pattern

# result=re.sub('Python','Java','Python is a good language to learn. I like learning Python. Python rocks.')
# print result


# result=re.sub('  ',' ','Python  is a good language           to learn. I like           learning Python. Python rocks.')
# print result



# # # 6- re.compile() - helps to create a pattern object
# #
# mypattern = re.compile('Python')
#
# result = mypattern.findall('Python is a good language to learn.')
# print result
#
# result = mypattern.findall('Python is a good language to learn. I like learning Python. Python rocks.')
# print result



