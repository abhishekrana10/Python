n=int(raw_input("Enter the number:"))

def dec_to_bin(x):
    if (x>1):
        dec_to_bin(x/2)
    print x%2,
    
dec_to_bin(n);
