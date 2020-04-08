import random

ob = open("new.txt","w")
how_many = int(input("enter how much you need : "))
start = int(input( "starting number : "))
end = int(input("end number : "))
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
    print('error found')
