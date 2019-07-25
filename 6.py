# Python program to calculate average, max, min of all valid numbers received from command line. 
import sys;
cnt=len(sys.argv)-1;
args=sys.argv;

avg=0;
i=1;
for i in range(cnt):
    print(int(args[i+1]));

for i in range(cnt):
    avg=avg+(int(args(i+1)));

print(avg);
