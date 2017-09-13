# CTI-110
# M2HW2
# Manuel Maldonado
# 09/13/2017

# area = lenght * width
# Calculate area of two rectangles

firstLength = int(input('What is the length of the first rectangle? '))

firstWidth = int(input('What is the width of first rectangle? '))

secondLength = int(input('What is the length of the second rectangle? '))

secondWidth = int(input('What is the width of the second rectangle? '))

# Calculate area (length * width)

firstArea = firstLength * firstWidth

secondArea = secondLength * secondWidth

#print('The area of the first rectangle is:', firstArea)

#print('The area of the second rectangle is:', secondArea)


# Compare the two areas

if firstArea > secondArea:
    print('The First rectangle is larger.')

elif firstArea < secondArea:
    print('The Second rectangle is larger.')

else:
    print('The two rectangles have the same area.')
