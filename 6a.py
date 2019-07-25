# Python program to calculate average, max, min of all valid numbers received from command line. 
import sys;
cnt=len(sys.argv)-1;
args=sys.argv;

avg=0;
i=1;
for i in range(cnt):
    print(int(args[i+1]));

for i in range(cnt):
    avg=avg+(int(args[i+1]));
max=int(args[1]);
for i in range(cnt):
    if(int(args[i+1]))>max:
        max=int(args[i+1]);

min=int(args[cnt]);
for i in range(cnt):
    if(int(args[i+1]))>min:
        min=int(args[i+1]);

tavg=avg//cnt;

        

print(avg);
print(max);
print(min);
