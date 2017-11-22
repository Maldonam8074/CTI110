# CTI-110-0002
# M6T1: Kilometer Converter
# Manuel Maldonado
# 10/23/2017


def main():

    # Miles = Kilometers * 0.6214

    # Program that asks for a distance in KM and converts to Miles
    # Should Include:
    # A main() function
    # A show_miles() function that takes KM as parameter and converts.
    # Then prints answer.

    # Get distance KM.
    kilometers = float(input("Please enter a distance in kilometers: "))

    # Display the converted distance
    show_miles(kilometers)

def show_miles(km):

    CONVERSION_FACTOR = 0.6214

    # Calculate Miles
    miles = km * CONVERSION_FACTOR

    # Display the miles (format to two decimals for looks)
    print(km, "Kilometers equals", format(miles, '.2f'), "miles.")

# Start Program
main()
