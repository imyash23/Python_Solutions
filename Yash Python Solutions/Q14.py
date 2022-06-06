# Q14. Finding GCD of 2 numbers ( O(log(min(a,b))) time and space) 

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

a=int(input("Enter first no"))
b=int(input("Enter second no"))
if (gcd(a,b)):
    print("Gcd of ",a,"and",b,"is",gcd(a,b))
else:
    print("not exist")
