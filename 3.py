#Python program to receive a “valid” number from command line argument and check whether it is prime or not
import sys;
arg=sys.argv;

num=int(arg[1]);

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number");
            print(i,"is a factor of ",num);
            break
        else:
            print(num,"is a prime number");
else:
    print (num,"is not a prime number");
