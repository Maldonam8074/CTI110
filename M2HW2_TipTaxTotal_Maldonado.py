#CTI-110
#M2HW2 - Tip Tax Total
#Manuel Maldonado
#09/04/2017

#tip = 0.18
#salesTax = 0.07
#taxAmount = lunchCost * salesTax

foodCost = float(input('How much was your meal? '))

tipAmount = 0.18 * foodCost

salesTax = 0.07 * foodCost

totalCost = foodCost + tipAmount + salesTax

print('Your tip amount is $', format(tipAmount, '.2f'))

print('Your tax amount is $', format(salesTax, '.2f'))

print('Your total is $', format(totalCost, '.2f'))


