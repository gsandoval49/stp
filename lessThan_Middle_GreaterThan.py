# took a long time to figure out the if and else statements on this one.
# the trick was to rearrange the statement
# instead of x < 10 >= 25
# i did 10 < x <= 25 and that did the trick.  

x = 50
if x <= 10:
    print ("at or not quite to 10")
if 10 < x <= 25:
    print ("it's in the middle")
else:
    print ("above 25, yes!")
        
