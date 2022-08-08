fruit = ["Apple", "Pear", "Orange"]

fruit.append("Banana") 
fruit.append("Tangerine")

#the append will always store the new at the end of the list

print(fruit)


#lists are not limited to storing strings
# they can store any data type

random = []
random.append(True)
random.append(100)
random.append(1.0)
random.append("hello")
print(random)


# i can use an index to retrieve it's place in a list
print(fruit[1])

### if you try to access an index that doesn't exist, python raises this exception
# print(fruit[8])

# you can change an item in a list by assigning it sindex to a new object
fruit[2] = 'kiwi'
print(fruit)

# you can remove the last item from a list using pop method
fruit.pop()
print(fruit)
