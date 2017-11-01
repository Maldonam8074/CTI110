# CTI 110-0002
# M6LAB
# Manuel Maldonado
# 30 October 2017

def main():
    

    # Ask user name, then ask age.
    # Then greet user by name and tell them their age. (infant, child, teenager, adult)
    # Use functions main(), greet(name), ageCategory(age).

    # Ask for name.
    name = input("Hello what is your name? ")

    # Run greet function
    greet(name)

    # Ask for age
    age = int(input("Now Please enter your age: "))

    # Final result for age.
    print("Seeing as you are", age,"this makes you", ageCategory(age))

# Function to greet user
def greet(name):
    
    # Result
    print("Hello", name)
        
# Function to tell user age category.
def ageCategory(age):

    # list of age values.
    adultAge = 20
    teenagerAge = 13
    childAge = 1
    infantAge = 0

    # Boolean expression using above data.
    if age >= adultAge:
        return "an Adult."

    else:
        if age >= teenagerAge:
            return 'a Teenager.'

        else:
            if age >= childAge:
                return 'a Child.'

            else:
                if age == infantAge:
                    return 'an Infant, should you be using a computer?'


# Start Program
main()
