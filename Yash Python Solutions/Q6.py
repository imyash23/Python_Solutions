# Q6. Find all prime no. in a given range.

def prime(x, y):
    list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                list.append(i)
    return list

starting = int(input("Enter starting range: "))
ending = int(input("Enter ending range: "))
lst = prime(starting, ending)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
