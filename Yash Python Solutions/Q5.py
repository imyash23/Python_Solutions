# Q5. Write a program in Python for finding that one number from an array of 100 numbers(with values ranging from 1 to 99) which is duplicate.

import array
array=[]
def fcn(array):
    for i in range(0, len(array)):    
        for j in range(i+1, len(array)):    
            if(array[i] > array[j]):    
                temp = array[i]  
                array[i] = array[j]    
                array[j] = temp  
    for j in range(100):
        if array[j]==array[j+1]:
            print(array[j])
fcn([1,2,3,4,5,6,5,]) 