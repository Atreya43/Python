#In above program 1, receive values of n1 and n2 from command line argument instead of taking them as an input from user

import sys;
args=sys.argv;

a=int(args[1]);
b=int(args[2]);

print(args[1]);
print(args[2]);

#a=int(input("Enter the lower limit for the range:"))
#b=int(input("Enter the upper limit for the range:"))
for i in range(args[1],args[2]+1):
    if(i%2!=0):
        print(i);

