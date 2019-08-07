# Develop a Python program to print odd numbers between n1 and n2. Input n1 and n2 from user

 
a=int(input("Enter the lower limit for the range:"))
b=int(input("Enter the upper limit for the range:"))
for i in range(a,b+1):
    if(i%2!=0):
        print(i);
