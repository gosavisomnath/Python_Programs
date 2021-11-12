"""
@Author: Somnath Gosavi
@Date: 2021-11-11 
@Title : To find the percentage of win and loss count .
""" 


from random import randint


class Gambler:
    def findPercentage(self):
    
     print("----------------Gambler program ------------------")
    stake =int(input("Enter the stake : "))
    goal = int(input("Enter the goals :"))

    countBet = 0
    winCount = 0
    lossCount = 0
    while True:

            if stake == 0 or stake == goal:
                break

            else:
                random_value = randint(0,1)
                countBet = countBet + 1

                if random_value == 1:
                    stake = stake + 1
                    winCount = winCount + 1
                    

                else:
                    stake = stake- 1
                    lossCount = lossCount + 1

    print("Number of wins : {}".format(winCount)) 
    print("Number of loss : {}".format(lossCount))               
    print("Percentage of win : ", (winCount / countBet) * 100)
    print("Percentage of loss : ", (lossCount / countBet) * 100)

gambler = Gambler()
gambler.findPercentage()  