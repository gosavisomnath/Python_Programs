'''
@author:Soma Gosavi
@Date:2021-09-11
@Last Modified by:Soma Gosavi
@Title: Power Of 2
'''

def find(num):
   if (num == 0):
      return False
   while (num != 1):
      if (num % 2 != 0):
         return False
      num = num // 2
   return True

num=int(input("Enter A number:"))
if(find(num)):
   print('Yes')
else:
   print('No')