# Test Grading Program
# 01 November 2017
# CTI-110 M6HW1 - Test Average and Grade
# Manuuel Maldonado

def main():

    # Program must ask user to enter 5 test grades.
    # Should then display a letter grade for each score.
    # Finally, it should give the average test score.
    
    grade = 0;

    # Created a range for the five grades.
    
    enter = range(1, 6)

    # Used a for loop to ask for scores individually.
    
    for num in enter:

        print('Please enter score', num,':')

        # Ask user for inputs of grades using input()
        
        score = int(input())

        # Call for determine_grade() function to convert number.
        
        determine_grade(score)

        # Formula to add all number grades.
        
        grade = grade + score

    # Added some space after final grade for formatting.

    print("")

    # Printed average number score using calc_average() function.

    print('Your average score is:', calc_average(grade))

    # Printed letter grade (Thank you for help with this part).

    determine_grade(calc_average(grade))


def calc_average(num):

    # Accept the 5 test scores (int or float) as arguments then return average.
    # To calculate, take total of all grades then divide by number of grades.

    # Formula to calculate average
    average = num / 5

    return average

def determine_grade(num):

    # Should accept a test score (int or float) as argument then return letter score.
    # Use grading scale from previous assignment grade should be a string (A,B,C,D, or F)

    # Bring the score into function using num.
    score = num

    # Reused a previous homework program here.
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
         print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    if score < D_score:
                                print('Your grade is: F')


# Start Program
main()
