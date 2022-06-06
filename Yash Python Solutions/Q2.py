# Q2.Write a function in Python that accepts a credit card number. 
# It should return a string where all the characters are hidden with an asterisk except the last four.
#  For example, if the function gets sent "4444444444444444", then it should return "4444".


x = int(input("number: "))
y = [int(x) for x in str(x)]
z = []
a = y[-1]
b = y[-2]
c = y[-3]
d = y[-4]
z.append(d)
z.append(c)
z.append(b)
z.append(a)
print(z)