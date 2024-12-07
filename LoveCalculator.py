x=input("Enter your name\n")
y=input("Enter your lover name\n")

x_lower=x.lower()
y_lower=y.lower()
your=x_lower.count("t")+x_lower.count("r")+x_lower.count("u")+x_lower.count("e")
Her=y_lower.count("t")+y_lower.count("t")+y_lower.count("u")+y_lower.count("e")
yoursecond=x_lower.count("l")+x_lower.count("o")+x_lower.count("v")+x_lower.count("e")
HerSecond=y_lower.count("l")+y_lower.count("o")+y_lower.count("v")+y_lower.count("e")

a=str(Her+your)
b=str(yoursecond+HerSecond)
c=a+b
d=int(c)
if d>50 :
    print(f"your love is {d}% greate you have true feeling for each other")
if 50>=d>10 :
  print(f"your love is {d}% you don't have true feeling for each other")
if d>80:
   print(f"you love is {d}% Awesome you are just like romeo and juliet ")