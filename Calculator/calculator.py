#improt your first a library regx:
#And first of all i tell you this is just a console application.
#I create another project how to build GUI Application
import re 
print("Our Magical Calculator")
print("type 'quit' and exit/n")
previous = 0
run = True
#create a mathmatical function
def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Type Equation:")
    else:
        equation = input(str(previous))
    
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z.,"":()]','',equation)
    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)
        print("Ans:", previous)
while run:
    performMath()
#Finish work
