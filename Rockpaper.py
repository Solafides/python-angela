import random
row=["rock","paper","scissors"]
computer=random.randint(0,2)
player=input("choose rock or paper or scissors\n")
play=player.lower()
if row[computer]==play :
    print(f"{row[computer]} you are equal")
elif row[computer]=="rock" and play==row[2]:
    print(f"{row[computer]} you lose ")
elif row[computer]=="rock" and play==row[1]:
    print(f"you won ")
elif row[computer]=="scissors" and play==row[1]:
    print("you lose")
elif row[computer]=="scissors" and play==row[0]:
    print(f"{row[computer]}\n you won")
else:
    print("you have inserted wrong name please try again later")