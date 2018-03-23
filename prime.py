import math

n=int(raw_input("Enter the number:"))

def prime_or_not(n):
    r=int(math.ceil(n**(1/2.0)))
    for num in range(2,r+1):
        if (n%num==0):
            print ("NOT PRIME")
            break
        elif (num==r):
            print ("PRIME")
            break
    return
    
prime_or_not(n);
    

