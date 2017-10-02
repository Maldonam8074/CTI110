# CTI-110
# M4T2 - Python Exercise
# Manuel Maldonado
# 10/02/2017

# Pyhon source code
# Should cover HTML tags <p>, <h1>, <b>, <div>

def main():

    # This program should ask the user to enter a tag then describe the tag.
    # If it's not one of these tags print "tag not found"

    pDescription = ('<p> is the paragraph tag, you would use it to group text into a paragraph.')
    pExample = ('Example of use: <p>text</p>')
    h1Description = ('<h1> is the largest header tag, you would use it to make the header font larger.  The higher the number, the smaller the font.')
    h1Example = ('Example of use: <h1>text</h1>')
    bDescription = ('<b> is the bold tag, you would use it to make your font bold.')
    bExample = ('Example of use: <b>text</b>')
    divDescription = ('<div> is the division tag, you would use it to define a division or section.  Can also be used to group block-elements to format them with css.')
    divExample = ('Example of use: <div style="color:#0000FF">text</div>')

    tag = input('PLease enter one of these tags p, h1, b, div: ')
    if tag == ('p'):
        print (pDescription)
        print (pExample)
    elif tag == ('h1'):
        print (h1Description)
        print (h1Example)
    elif tag == ('b'):
        print (bDescription)
        print (bExample)
    elif tag == ('div'):
        print (divDescription)
        print (divExample)
    else:
        print('Tag not found')

# Start Program
main() 
