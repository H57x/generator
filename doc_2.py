from colored import fg,bg,attr
color_1=fg("#e81b05")
color_2 =fg("white")
color_3 = fg("#01910b")
color_4 =fg("#9f12db")
reset = attr("reset")
print(color_1+"   _____ ______ _   _ ______ _____         _______ ____  _____ ")
print(color_1+"  / ____|  ____| \ | |  ____|  __ \     /\|__   __/ __ \|  __ \ ")
print(color_2+" | |  __| |__  |  \| | |__  | |__) |   /  \  | | | |  | | |__) |")
print(color_2+" | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | | | |  | |  _  /")
print(color_3+" | |__| | |____| |\  | |____| | \ \  / ____ \| | | |__| | | \ \ ")
print(color_3+"  \_____|______|_| \_|______|_|  \_\/_/    \_\_|  \____/|_|  \_\ "+reset)
print(color_4+"\n\t\t\t\t\t\t\t              scripted by -//sh4d0w"+reset)
import os
print("1. run to generate \n2. exit")
call = input("choose: ")
if call == "1":
    try:
        os.system("python3 dot.py")
    except:
        print("error")
else:
    print("thankyou!")