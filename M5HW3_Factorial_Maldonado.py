# CTI-110
# M5HW3: Factorial
# Manuel Maldonado
# 10-16-2017

# n! = n × (n−1)!
# So 10! = 10 × 9!, ... and 125! = 125 × 124!, etc.


def main():
    # A program that asks user to input a number then gives factorial of number.
    
    # ask for input and give variables value
    integer = int(input("Please enter a non-negative integer? "))

    factorial = 1

    # Statements to stop user from trying to outsmart program
    if integer < 0:
        print("Please enter a positive number")

    elif integer == 0:
        print("The factorial of 0 is 1")

    else:

        # Loop to perform math.
        for i in range(1, integer + 1):
            factorial = factorial * i

        # print answer out for user.
        print("The factorial of ", integer, " is ", factorial)
        
# Start Program
main()
