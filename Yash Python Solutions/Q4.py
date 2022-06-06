# Q4.Create a Python function that accepts a string. 
# The function should return a string, with each character in the original string doubled.
# If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!"

def duplicate(str):
    c=len(str)
    for i in range(0,c):
       print(str[i]*2,end="") 
duplicate("Roboism") 
