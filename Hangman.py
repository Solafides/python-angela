import random
words=["fire","water","soil","light","ferest","ocean"]
chosen=random.randint(0,len(words))
chosenWord=words[chosen]
# listchosen=chosenWord.split(",")
# print(listchosen)
print(chosenWord)
noOfwords=len(chosenWord)
emptywords=[]
print(noOfwords)
i='_'
for letter in range(noOfwords):
    
    emptywords.append(i)
    # if letter==input_word:

    #     print(f"{letter}")
    # else:
    #     print("*")
print(emptywords)
counter=len(emptywords)
input_word=input("\nGuess the word\n")
end=False
while not end:
 for index,letter in enumerate(chosenWord) :
        
        if letter== input_word:
            # for x in chosenWord:
            emptywords[index]=letter
            print(emptywords)
            input_word=input("\nGuess the word\n")
 if input_word not in chosenWord:
            counter-=1
            if counter==0:
                print("you lose")
                break
            print(f"you have {counter} chance")
           
            input_word=input("\nGuess the word\n")
           
 if "_" not in emptywords :
           end=True
           print("you won")        
 
       

    
   