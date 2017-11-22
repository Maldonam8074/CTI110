# A program that converts distance from feet to inches.
# 10/25/2017
# CTI-110 M6T2_FeetToInches
# Manuel Maldonado

def main():

# inches = feet * 12
# Program should use value-returning function.
# Asks user to input distance in feet, then print distance in inches.
# Use main() and feet to inches() functions.

    # Constant for inches, instead of just using 12 for inches.
    INCHES_PER_FOOT = 12

    # Ask for input and link to feet.
    feet = int(input("Please enter a distance in feet: "))

    # Define the function
    def feet_to_inches(feet):

        # Formula to convert feet to inches.
        return feet * INCHES_PER_FOOT

    # Print the answer
    print(feet, "eguals", feet_to_inches(feet), "inches")

        
# Start the Program
main()
