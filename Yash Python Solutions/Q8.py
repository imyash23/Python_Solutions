# Q8. Python program to calculate sum of integers in string 
# (eg. S = “h20 15 wa73r”, so sum will be 2+0+1+5+7+3).

def sum(str1):
    temp="0"
    sum=0

    for ch in str1:
        if(ch.isdigit()):
            temp += ch
        else:
            sum += int(temp)
            temp = "0"
    return sum + int(temp)

str1="232fmggmr78"
print(sum(str1))