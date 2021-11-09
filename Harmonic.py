'''
@author:Soma Gosavi
@Date:2021-09-11
@Last Modified by:Soma Gosavi
@Title: Harmonic Number
'''
def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))
    
print(harmonic_sum(7))

