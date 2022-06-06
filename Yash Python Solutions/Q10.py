# Q10.  Python program to swap two numbers using xor.


x=int(input("Enter vallue of x : "))
y=int(input("Enter vallue of y : "))

x=x^y
y=x^y
x=x^y

print("value of x: ",x)
print("value of y: ",y)

