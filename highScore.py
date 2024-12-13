score=input("insert number of scores\n")
scores=score.split(" ")
max=scores[0]
for i in range(0,len(scores)):
   if(max<scores[i]):
      max=scores[i]
print(max)

#another easy method is using max() function sum() functions 
# print(max(scores))