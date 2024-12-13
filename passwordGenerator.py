import random
letters=["A","B","C","D","E","F","G","H","I","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols=["!","@","#","$","%","^","&","*","(",")","_","+"]
numbers=["1","2","3","4","5","6","7","8","9","0"]

# pw=random.randint(0,52)
password=[]
n=input("how many letters you want\n")
n2=input("how many symbols you want\n")
n3=input("how many numbers you want\n")
for i in range(0,int(n)):
    x=random.choice(letters)
    password.append(x)
for i in range(0,int(n3)):
    y=random.choice(numbers)
    password.append(y)
for i in range(0,int(n2)):
    z=random.choice(symbols)
    password.append(z)
random.shuffle(password)
w=""
for i in range(0,len(password)):
    w=w+password[i]
print(w)