# Q7. Python Program to find the highest frequency element in the array.
def freq(a,x):
    count=0
    for i in a:
        if i==x:count+=1
    return count

a=[1,25,25,14,1,4,25,3,25,25]
x=25
print(freq(a,x))