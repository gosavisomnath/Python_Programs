import re
'''
@author:Soma Gosavi
@Date:2021-09-11
@Last Modified by:Soma Gosavi
@Title: UserInput From User
'''

username = input("Enter username:")
reg=".*[a-zA-Z]{3}"
pat=re.compile(reg)
mat=re.search(pat,username)
if mat:
    print("Hello,\t"+username+"\tHow are you")
else:
    print("UserNAme has min 3 char")