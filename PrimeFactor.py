'''
@author:Soma Gosavi
@Date:2021-09-11
@Last Modified by:Soma Gosavi
@Title: Harmonic Number
'''
n = int(input("Enter the number:"))
for i in range(2,n + 1):
    if n % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            print(i)