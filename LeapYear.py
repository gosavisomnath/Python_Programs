'''
@author:Soma Gosavi
@Date:2021-09-11
@Last Modified by:Soma Gosavi
@Title: Leap Year
'''
def check_leap_year():
    
        year=input("Enter Year:")
        if len(year)==4:
            if int(year)%4==0:
                print(year,"is a leap year")
            else:
                print(year,"is not leap year")
        else:
            print("please enter 4 digit number!!")
    

check_leap_year()