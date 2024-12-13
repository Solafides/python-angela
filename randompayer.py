import random
split=input("enter your name separated by comma\n\n")
splitter=split.split(",")

length=len(splitter)

name=random.randint(0,length-1)

print(f"Today's Bill payer is {splitter[name]}")

# the choice(splitter) method can do all of this