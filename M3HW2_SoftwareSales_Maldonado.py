# CTI-110
# M2HW2-Software Sales
# Manuel Maldonado
# 09/19/2017

# Software retails at $99

# Discounts if bought in bulk
# 10 - 19: 10% Discount
# 20 - 49: 20% Discount
# 50 - 99: 30% Discount
# 100+: 40% Discount

def main():
    # This program will give the price of purchases including dicsounts.

    units = float(input('How many packages are you purchasing? '))
    swPrice = 99
    noDiscount = units * swPrice
    tenPercent = noDiscount / 10
    discountTen = (units * swPrice) - tenPercent
    twentyPercent = noDiscount / 20
    discountTwenty = (units * swPrice) - twentyPercent
    thirtyPercent = noDiscount / 30
    discountThirty = (units * swPrice) - thirtyPercent
    fourtyPercent = noDiscount / 40
    discountFourty = (units * swPrice) - fourtyPercent
    

    if units >= 100:
        print('You qualify for our maximum discount of 40%, your discounted price is: $', format(discountFourty, '.2f'))
    else:
        if units <= 99 and units >= 50:
            print('You qualify for a 30% discount, your discounted price is: $', format(discountThirty, '.2f'))
        else:
            if units <= 49 and units >= 20:
                print('You qualify for a 20% discount, your discounted price is: $', format(discountTwenty, '.2f'))
            else:
                if units <= 19 and units >= 10:
                    print('You qualify for a 10% discount, your discounted price is: $', format(discountTen, '.2f'))
                else:
                    if units < 10:
                        print ('You do not qualify for a discount, your price is: $', format(noDiscount, '.2f'))
        
    
# Program Start    
main()
