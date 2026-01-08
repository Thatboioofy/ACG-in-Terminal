import keyboard
import time
import os
import random
from termcolor import cprint
menu = "main"


def MainScreen(menu):
    loop = True
    CoreTemp = 0
    print("PRC Managment System v0.1")
    print("Solaris Copyright 1999")
    print("\n")
    while loop == True:
        CoreTemp = CoreTemp + random.randint(20,100)
        if menu == "main":
            if CoreTemp >3000:
                cprint("Reactor Tempreture : " + str(CoreTemp), 'red', end='\r')
            elif CoreTemp >2500:
                cprint("Reactor Tempreture :" + str(CoreTemp), 'light_red', end='\r')
            elif CoreTemp < 50:
                cprint("Reactor Tempreture :" + str(CoreTemp), 'cyan', end='\r')
            else:
                print("Reactor Tempreture :" + str(CoreTemp), end='\r')
            if keyboard.is_pressed("c") == True:
                menu = "Coolent"
        if menu == "Coolent":
            print("Coolent Configuration")
            Position = 1
            if keyboard.is_pressed("m") == True:
                menu = "main"
            if keyboard.is_pressed("down") == True:
                if Position >= 5:
                    Position = 5
                else:
                    Position = Position +1
            if keyboard.is_pressed("up") == True:
                if Position <= 1:
                    Position = 1
                else:
                    Position = Position -1
            
            print("Coolent Pump 1", end='\r')
            print("Coolent Pump 2", end='\r')
            print("Coolent Pump 3", end='\r')
            print("Coolent Pump 4", end='\r')
        

            



def Startup(error, menu):
    dots = "."
    cprint("Solaris OS v1.0", 'green')
    print("Cpu : Intel Pentium")
    print("RAM : 1024 MB")
    print("BIOS ver : 1999.02")
    print("\n \n")
    if error == "UNSHUT":
        print("System went though an unexpected shutdown \n")
        for i in range(10):
            print("Checking Filesystem" +dots, end='\r')
            dots = dots + "."
            time.sleep(.2)
        print("Filesystem Check Complete \n")
        dots = "."
        


    for i in range(10):
        print("Booting" + dots, end='\r')
        dots = dots + "."
        time.sleep(random.uniform(0.1, 0.5))

    os.system('cls')
    MainScreen(menu)
Startup("", menu)


            



