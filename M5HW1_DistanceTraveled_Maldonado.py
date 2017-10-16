# CTI-110
# M5HW1: Distance Traveled
# Manuel Maldonado
# 10-11-2017

def main():

# distance = speed * time
# program that asks user speed of vehicle and number of hours traveled.
# Then display distance traveled for each hour of that time period.
# Display in table format.

    
    # Ask for speed from user.
    speed = int(input("What speed was the vehicle traveling? "))

    print()
    
    # ask for time variable.
    hours = int(input("How many hours did you drive? "))

    print()

    # Heading for chart
    print("Hours\tDistance Traveled")
    print("-------------------------") 

    # Loop to perform math
    for time in range(1, 1 + hours):

        # Formula
        distance = speed * time

        # Results
        print(time, "\t" ,distance, "Miles")    


main()
