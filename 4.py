import sys;
arg=sys.argv;
x=int(arg[1]);
y=int(arg[2]);
#x=int(input("Enter the value of x: "));
#y=int(input("Enter the value of y: "));

print("Prime numbers between",x,"and",y,"are:")

for num in range(x,y + 1):
  if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num);
