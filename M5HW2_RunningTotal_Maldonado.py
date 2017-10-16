# CTI-110
# M5HW2: Running Total
# Manuel Maldonado
# 10-11-2017

def main():
    # A program that asks user a number until user enters a negative number.
    # then ends loop and adds all numbers except negative entry.
    
    runningTotal = 0

    keepGoing = True

    # Loop
    while keepGoing:

        # Ask user for a number
        print("PLease enter a number? ")

        number = int(input())

        
        if number < 0:
            keepGoing = False

        # Closing the loop
        else:
            runningTotal = runningTotal + number

    print("Total is: ", runningTotal)

# Start Program
main()
