#Develop a menu-based python program (menu items: 1. Addition 2. Subtraction 3. Multiplication
#4. Division 5. Average 6. Find maximum 7. Find minimum) for a numeric list.
def PrintMenu():
    print("1)Addition")
    print("2)Subtraction")
    print("3)Multiplication")
    print("4)Division")
    print("5)Average")
    print("6)Find Maximum")
    print("7)Find Minimum")

def GetChoice():
    choice=int(input("Enter the choice:"));
    return(choice);

def Add(lst):
    sm = sum(lst);
    return sm;
def sub(lst):
    subtraction=0;
    for i in lst:
        subtraction = int(i) - subtraction

    return subtraction

PrintMenu();
ch=GetChoice();

lst=[2,3];
if(ch==1):
    ans = add(lst);
    print(ans);
elif(ch==2):
    ans = sub(lst);
    print(ans);

    def Choice(ch):
    if ch == 1:
        print("Addition for Numeric List",add(list1))
    elif ch == 2:
        print("Subtraction for Numeric List",sub(list1))
    elif ch == 3:
        print("Multiplication for Numeric List",mul(list1))
    elif ch == 4:
        print("Division for Numeric List",Div(list1))
    elif ch == 5:
        print("Average for Numeric List",Avg(list1))
    elif ch == 6:
        print("Maximum for Numeric List",Max(list1))
    elif ch == 7:
        print("Minimum for Numeric List",Min(list1))
    elif ch == 8:
        break
        
