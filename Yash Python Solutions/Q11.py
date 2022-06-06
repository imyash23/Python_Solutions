# Q11. Write a Python Program to Check if a String is a Palindrome or Not


def palindrome(s):
    return s==s[::-1]

s=input("Enter word: ")
y=palindrome(s)

if y:
    print("YES")
else:
    print("NO")