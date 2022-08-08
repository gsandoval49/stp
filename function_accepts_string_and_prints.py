a = input("enter a string:")

"""
take input as a string
since all inputs are taken as strings
there wasn't a need to convert to a string
but if somehow something wasn't a string
the else block would say not a string
"""

if str:
    print(a)
else:
    print ("this is not a string.")
    

# alternative
"""
this was the solution to the challenge
we define a function and set the variable as a string
then we call the fucntion below
"""

def print_string(string):
    print(string)

print_string("Testring: 1,2,3.")

    
