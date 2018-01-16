import re

# Variable Patterns
# For documentation refer to the below link
# https://docs.python.org/2/library/re.html



# # '.' - Matches with any single character except newline \n.
# result=re.findall('.','Python is a good language to learn. I like learning Python. Python rocks.')
# print result

#
# # # '\w' & '\W' - Matches with any single character except newline \n.
# result2=re.findall('\W','Python is a good language to learn. I like learning Python. Python rocks.')
# print result2

# # # '*' & '+' - Matches with any single character except newline \n.
# #
# result3=re.findall('\w*','Python is a good language to learn. I like learning Python. Python rocks.')
# print result3
#
# result3=re.findall('\w+','Python is a good language to learn. I like learning Python. Python rocks.')
# print result3

# ^ and $ match the start or end of the string respectively

# result4 = re.findall('^\w+','Python is a good language to learn. I like learning Python. Python rocks.')
# print result4
#
# result4 = re.findall('\w+$','Python is a good language to learn. I like learning Python. Python rocks')
# print result4




# # Finding 3 consecutive characters for each word
# #
# result5 = re.findall('\w\w\w','Python is a good language to learn. I like learning Python. Python rocks.')
# print result5
#
# # '\b' - boundary
# result6 = re.findall('\\b\w\w\w','Python is a good language to learn. I like learning Python. Python rocks.')
# print result6



# # Finding domain name in an Email address
#
# result=re.findall('@\w+','abc_xyz@gmail.com, xyz.pqr@msn.com, python@yahoo.com, data.sience@edureka.in,blank@')
# print result


# # Get domain names only
# result=re.findall('\w+\W*\w+@\w+\.\w+','abc_xyz@gmail.com, xyz.pqr@msn.com, python@yahoo.com, data.sience@edureka.in,blank@')
# print result

# # Get domain and extension
# result=re.findall('(\w+\.\w+)','abc_xyz@gmail.com, xyz.pqr@msn.com, python@yahoo.com, data.sience@edureka.in,blank@')
# print result

# # Find a date & IP Address from a string of Server Log
# #
# result=re.findall('\d{1,3}\.\d{1,3}\.\d{2,3}\.\d{2,3}','123.1.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"')
# print result

# # # Date Time
# result=re.findall('\d{1,2}/\w\w\w/\d{4}:\d{2}:\d{2}:\d{2}','123.1.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"')
# print result


# # # Find a valid Phone number
# result = re.findall('\W+\d{1}\W+\d{3}\W+\d{3}\W+\d{4}','hi! you can message me on +1-541-754-3010')
# print result
#

# # Find a Hashtag in a text
# result = re.findall('\#\w+','Python is a good language to learn. #Python, #edureka')
# print result


# # Parse data from a XML/HTML file
#
# htmlstr = """<tr align="center"><td>1</td> <td>Noah</td> <td>Emma</td></tr>
# <tr align="center"><td>2</td> <td>Liam</td> <td>Olivia</td></tr>
# <tr align="center"><td>3</td> <td>Mason</td> <td>Sophia</td></tr>
# <tr align="center"><td>4</td> <td>Jacob</td> <td>Isabella</td></tr>
# <tr align="center"><td>5</td> <td>William</td> <td>Ava</td></tr>
# <tr align="center"><td>6</td> <td>Ethan</td> <td>Mia</td></tr>
# <tr align="center"><td>7</td> <td HTML>Michael</td> <td>Emily</td></tr>"""
#
# result = re.findall(r'<td>(\d)</td>\s<td>(\w+)</td>\s<td>(\w+)</td>',htmlstr)
# print result



