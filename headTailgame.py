import random
print("hello there this is random head or tail game\n")


c=random.randint(0,1)
a=input("Head or Tail ?\n")
b=a.lower()
if b=="head":
    x=1
    if x==c:
       print("you won")
    else:
       print("you lose")
elif b=="tail":
    x=0
    if x==c:
       print("you won")
    else:
       print("you lose")
else:
    print("you have entered wrong name")
