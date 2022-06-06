# Q1. Create a function in Python that accepts two parameters. 
# The first will be a list of numbers. 
# The second parameter will be a string that can be one of the following values: asc, desc, and none.
# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.


x = int(input("list of numbers: "))
y = input("asc, desc, none: ")
res = [int(x) for x in str(x)]
if y == "asc":
    res.sort()
print(str(res))
if y == "desc":
    res.sort(reverse=True)
print(str(res))
if y == "none":
    print(str(res))