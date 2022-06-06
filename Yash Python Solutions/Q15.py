# Q15. Python program to count alphabets, digits and special characters in a string.
str =input("Enter ur string : ")
alphabets=digits=special=0

for i in range(len(str)):
    if(str[i].isalpha()):
        alphabets=alphabets+1
    elif(str[i].isdigit()):
        digits=digits+1
    else:
        special=special+1

print("Total no of alphabets in str:",alphabets)
print("Total no of digits in str:",digits)
print("Total no of special in str:",special)
