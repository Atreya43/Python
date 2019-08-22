#Develop a menu-based python program
#menu items: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Average 6. Find maximum 7. Find minimum
import sys
def PrintMenu():
    print("Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Average")
    print("6. Find maximum")
    print("7. Find minimum")
    print("8. Append ");
    print("9. Mean")
    print("10. Mode")
    print("8.Exit")

def add(lst):
   return sum(lst);

def sub(lst):
    subtraction=0;
    for i in lst:
        subtraction = int(i) - subtraction;

    return subtraction;
def mul(lst):
    mul=1
    for i in lst:
        mul = mul * int(i);

    return mul;
def Div(lst):
    div=1;
    div = lst[0]/lst[1];
    return div;

def Avg(lst):
    a = sum(lst);
    b = len(lst);
    avg = a/b;
    return avg;

def Max(lst):
    return max(lst);

def Min(lst):
    return min(lst);

def Append(lst):
    lst.append(5)
    print("Appended list is:");
    print(lst);

def Mean(lst):
    a = sum(lst);
    b = len(lst);
    mn = a/b;
    return mn;

def Mode(lst):
    lst.sort()
    lst
    
def GetChoice():
    ch = int(input("Enter Choice : "));
    return ch;

def repeate():
    while True:
        PrintMenu()
        ch=GetChoice()
        Choice(ch)

def Choice(ch):
    if ch == 1:
        print("Sum of List=",add(lst));
    elif ch == 2:
        print("Subtraction of List=",sub(lst));
    elif ch == 3:
        print("Multiplication of List=",mul(lst));
    elif ch == 4:
        print("Division of List=",Div(lst));
    elif ch == 5:
        print("Average of List=",Avg(lst));
    elif ch == 6:
        print("Maximum of List=",Max(lst));
    elif ch == 7:
        print("Minimum of List=",Min(lst));
    elif ch == 8:
        print("Append:",Append(lst));
    elif ch == 9:
        print("Mean of the list=",Mean(lst));
    elif ch == 10:
        print("Mode=",Mode(lst));
    else:
        print("Enter the Valid Choice");



lst = [1,5,6,3,5,2,4]
repeate()





