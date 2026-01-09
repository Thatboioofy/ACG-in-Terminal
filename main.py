import keyboard
import time
import os
import random
from pick import pick
from termcolor import cprint
menu = "main"
Sys_Int = True

#Code still in really early Development and everything IS broken


def CoolentPumps(PumpNum, Pump_Strain, Pump_Strength):
    print()







def MainScreen(menu, Sys_Int):
    loop = True
    CoreTemp = 0
    print("PRC Managment System v0.1")
    print("Solaris Copyright 1999")
    print("\n")
    if Sys_Int == True:
        Sys_Int = False
        default_Pump_Strength = 5 # Sets initial pump speeds (NOTE : 7.5 will start cause the pumps to gain strain)
        enable_pump_strain = True

        Pump1_Strain = 0
        Pump1_Strength = default_Pump_Strength
        
        Pump2_Strain = 0
        Pump2_Strength = default_Pump_Strength
        
        Pump3_Strain = 0
        Pump3_Strength = default_Pump_Strength
        
        Pump4_Strain = 0
        Pump4_Strength = default_Pump_Strength
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
            if keyboard.is_pressed("q") == True:
                Startup('UNSHUT', 'main')
        if menu == "Coolent":
            option = pick(['Coolent Pump 1', 'Coolent Pump 2', 'Coolent Pump 3', 'Coolent Pump 4'], 'Coolent Configuration')



        

            



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
    MainScreen(menu, Sys_Int)
Startup("", menu)


            



