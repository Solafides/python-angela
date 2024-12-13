word=input(f"ener the word you want to be encrypted\n")
text=word.upper()

shift=int(input("enter the shift code\n"))
letters=["A","B","C","D","E","F","G","H","I","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
encrypt=[]
indx=0
def ceasar(text,shift):
    for letter in text:
       if letter in letters:
         index=letters.index(letter)
         if index>25:
            index=0
         encrypt.append(letters[index+shift])
    print(f"your encrypted text is {encrypt}")
ceasar(text,shift)