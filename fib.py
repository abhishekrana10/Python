a=0
b=1

def fib(a,b,n):
    print a
    print b
    for num in range(1,n-1):
        f=a+b
        a=b
        b=f
        print f
    return
        
n=int(raw_input("How many terms of fibonacci series do you want:"))
fib(a,b,n);
