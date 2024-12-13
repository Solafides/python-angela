coverage=5
def paint(height,width):
    noOfCan=(int(height)*int(width))/coverage
    print(f"you need {round(noOfCan)} cans of paint")
paint(input("enter the height\n"),input("enter the width\n"))