import random
from colored import fg,bg,attr
color_1 = fg("red")
color_2 = fg("#f5f511")
ob = open("new.txt","w")
try:
    how_many = int(input("enter how much you need : "))
    start = int(input("starting number : "))
    end = int(input("end number : "))
except:
    print(color_2+"You have to put value")

def generator():
    for i in range(how_many):
        number = random.randrange(start,end)
        number=str(number)
        ob.write(number)
        ob.write("\n")
    ob.close()
try:
    generator()
    print("succes")
except:
    print(color_1+'Error Found!')
