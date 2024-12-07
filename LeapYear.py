a=int(input("please enter the year to be checked if it is leap year or not \n"))
if a%4==0:
 if a%100==0:
  if a%400==0:
   print(f"{a} is a leap year")
  else:
   print(f"{a} Is not a leap year")
 else:
  print(f"{a} is a leap year")
   
 

    
    
