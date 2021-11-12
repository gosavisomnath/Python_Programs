"""
@Author: somnath Gosavi
@Date: 2021-11-11 
@Title : To perform the stopwatch program and find the elapsed time .
""" 

class watch:

    def findElapedTime(self):
       
       print("stopwatch application is executed!\n")

    startTime = float(input("Enter startTime : "))
    endTime = float(input("Enter end time "))
    
   #calculating hour
    hour = endTime - startTime

    #calculating time in minutes
    startMin = startTime * 60
    endMin = endTime * 60
    min = endMin - startMin

    #claculating time in seconds
    startSec = startTime *3600
    endSec = endTime *3600
    sec = endSec - startSec

     #calculating time in milliseconds
    startMilliSec = startTime*3600*1000
    stopMilliSec = endTime *3600*1000
    milliseconds = stopMilliSec - startMilliSec
           
    print("Elapsed Time : {}:{}:{}:{} ".format(hour,min,sec,milliseconds))
        
obj = watch()
obj.findElapedTime()