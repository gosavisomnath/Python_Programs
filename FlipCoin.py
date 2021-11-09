import random
'''
@author:Soma Gosavi
@Date:2021-09-11
@Last Modified by:Soma Gosavi
@Title: FlipCoin
'''

def flipCoin(num):
    heads = 0 
    tails = 0 
    headspercent = 0 
    tailspercent = 0 

    for i in range(num): 
      coin=random.random()
      if coin<0.5: 
          tails+=1 
      else: 
          heads+=1

    headspercent = heads / 10.0
    tailspercent = 100.0 - headspercent 
    

    print("Heads percent: " + str(headspercent)) 
    print("Tails percent: " + str(tailspercent)) 

try:
    num = int(input("Enter Number:"))
    assert num>0
    flipCoin(num)
except AssertionError:
        print("Number is negative")
