n=int(raw_input("Enter the number:"))
x=n
sum=0;

while(n>0):
    r=n%10
    n=n/10
    sum=sum+(r**3)
  
if (x==sum):
    print("ARMSTRONG NUMBER")
else:
    print("NOT ARMSTRONG NUMBER")
