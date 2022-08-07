# write a function that converts a string to a float

# returns the result

# use exception handling for a scenario that could occur

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("We could not convert the string to a float")

c = convert("55.0")
print(c)
