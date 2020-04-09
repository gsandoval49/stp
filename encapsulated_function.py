# Functions can encapsulate functionality you want to reuse: 

def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

# reused  

even_odd(2)
even_odd(4)
even_odd(7)
even_odd(22)
even_odd(8)

# output should be >>> even, even, odd, even, even
