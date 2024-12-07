a=int(input("please enter the year to be checked if it is leap year or not \n"))
if a%4==0 and a%100!=0 and a%400!=0:
 print(f"{a} is a Leap year")
else :
 print(f"{a} is not a Leap year")
    