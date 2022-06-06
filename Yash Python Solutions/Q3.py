# Q3. Write a Python function that accepts three parameters. 
# The first parameter is an integer.
# The second is one of the following mathematical operators: +, -, /, or . 
# The third parameter will also be an integer.
# The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.


def calculator(a,b,c):
    if b=="+":
        return(a+c)
    elif b=="-":
        return(a-c)
    elif b=="*":
        return(a*b)
a=int(input("Enter value of a "))
c=int(input("Enter value of c "))
print(calculator(a,"+",c))