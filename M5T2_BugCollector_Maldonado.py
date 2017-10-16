# CTI-110-0002
# M5T2: Bug Collector
# Manuel Maldonado
# 9 October 2017

# Program that calculates running total of bugs collected in 7 day period.
# Use loop (for loop) ask number of bugs collected for that day.
# When loop is finished program should display total bugs collected.
# Todays Bugs
# Total Bugs

def main():
    # Program asks bugs collected daily then gives weekly total.

    totalBugs = 0;

    week = range(1, 8)

    # Get the bugs collected for each day.
    for day in week:

        # Prompt user.
        print("Enter the bugs collected on day", day)

        # Input number of bugs.
        todaysBugs = int(input())

        # Add bugs together
        totalBugs = totalBugs + todaysBugs

    # Display the total bugs.
    print("You collected a total of", totalBugs, "bugs.")
    
# Program Start
main()
