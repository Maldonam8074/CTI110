# CTI-110
# M3HW1 - Age Classifier
# Manuel Maldonado
# 09/18/2017

# ask user for a persons age
# display whether they are infant, child, teenager, or an adult.

# 1 year old or less = infant
# older than 1, but younger than 13 = child
# older than 13, but younger 20 = teenager
# older than 20 = adult

def main():
    # This program should ask user the age then state classification.

    adultAge = 20
    teenagerAge = 13
    childAge = 1
    babyAge = 0

    age = float(input('How old is this person?  Enter 0 if younger than 1. '))
    if age >= adultAge:
        print('This person is an Adult.')
    elif age == babyAge:
        float(input('How many months old is this person? '))
        print('This person is an infant.')
        
    else:
        if age >= teenagerAge:
            print('This person is a teenager.')
        else:
            if age >= childAge:
                print('This person is a child.')
            else:
                if age < childAge:
                    print('This person is an Infant.')


# Program start
main()
