import time
import AirConditioner as a
import HomeTheatre as h
import Laptop as l
import Mobile as m
import PowerBank as p
import SmartWatch as s
import Television as t

#Function to list all models of a particular gadget
def listData(device, label):
    try:
        f = open(device, "r")

        print("\n")
        print("********************************************************************************")
        print("* S.NO *      BRAND      *      MODEL      *      PRICE      *   RELEASE YEAR  *")
        print("********************************************************************************")
    
        #Loop to read lines from files of all models of a particular gadget and getting details required
        i = 1
        for x in f:
            x = x.rstrip('\n')
            f1 = open(label + x + ".txt", "r")
            print("")
            print(" ",format(i,"4d"),end = "")
            i = i + 1
        
            j = 1
            for y in f1:
                y = y[y.find(':') + 2:]
                y = y.rstrip('\n')
                print("  ",format(y,">15s"),end = "")
                j = j + 1
            
                if(j>4):
                    break

            print("")
            
            f1.close()
        
        f.close()

        #Getting user choice to display a particular model    
        ch = 0
        if i != 1:
            print("\n")
            ch = int(input("                            ENTER YOUR CHOICE : "))
        
            if ch > i-1:
                print("")
                print("                    ****************************************")
                print("                    *          INVALID CHOICE !!!          *")
                print("                    ****************************************")
                return ""
        else:
            print("")
            print("                    ****************************************")
            print("                    *        DEVICES UNAVAILABLE !!!       *")
            print("                    ****************************************")
            return ""
            
        f = open(device, "r")
        
        i = 1
        for x in f:
        
            if i >= ch:
                break

            i = i + 1

        f.close()
    
        x = x.rstrip('\n')
        return x
    except:
        print("")
        print("                    ****************************************")
        print("                    *        DEVICES UNAVAILABLE !!!       *")
        print("                    ****************************************")
        return ""

#Function accessible only by admin to add new model
def addDevice():
    print("\n\n")
    print("                    ****************************************")
    print("                    *              GADGET FINDER           *")
    print("                    ****************************************")
    print("                    |                                      |")
    print("                    |    1. AIR CONDITIONER                |")
    print("                    |                                      |")
    print("                    |    2. HOME THEATRE                   |")
    print("                    |                                      |")
    print("                    |    3. LAPTOP                         |")
    print("                    |                                      |")
    print("                    |    4. MOBILE                         |")
    print("                    |                                      |")
    print("                    |    5. POWER BANK                     |")
    print("                    |                                      |")
    print("                    |    6. SMART WATCH                    |")
    print("                    |                                      |")
    print("                    |    7. TELEVISION                     |")
    print("                    |                                      |")
    print("                    |    8. GO BACK                        |")
    print("                    |______________________________________|")

    print("\n")
    choice = int(input("                            ENTER YOUR CHOICE : "))

    t = 1
    
    if choice == 1:
        obj = a.AirConditioner()
        obj.getInput()
    elif choice == 2:
        obj = h.HomeTheatre()
        obj.getInput()
    elif choice == 3:
        obj = l.Laptop()
        obj.getInput()
    elif choice == 4:
        obj = m.Mobile()
        obj.getInput()
    elif choice == 5:
        obj = p.PowerBank()
        obj.getInput()
    elif choice == 6:
        obj = s.SmartWatch()
        obj.getInput()
    elif choice == 7:
        obj = t.Television()
        obj.getInput()
    elif choice == 8:
        homepage()
    else:
        t = 0
        print("")
        print("                    ****************************************")
        print("                    *          INVALID CHOICE !!!          *")
        print("                    ****************************************")
        print("\n")
        print("                           ",end = '')
        pause = input("PRESS ENTER TO CONTINUE...")
        addDevice()
        
    if t == 1:
        print("\n")
        print("                           ",end = '')
        pause = input("PRESS ENTER TO CONTINUE...")
        addDevice()

#Function to view details of a particular model
def viewDevice():
    print("\n\n")
    print("                    ****************************************")
    print("                    *              GADGET FINDER           *")
    print("                    ****************************************")
    print("                    |                                      |")
    print("                    |    1. AIR CONDITIONER                |")
    print("                    |                                      |")
    print("                    |    2. HOME THEATRE                   |")
    print("                    |                                      |")
    print("                    |    3. LAPTOP                         |")
    print("                    |                                      |")
    print("                    |    4. MOBILE                         |")
    print("                    |                                      |")
    print("                    |    5. POWER BANK                     |")
    print("                    |                                      |")
    print("                    |    6. SMART WATCH                    |")
    print("                    |                                      |")
    print("                    |    7. TELEVISION                     |")
    print("                    |                                      |")
    print("                    |    8. GO BACK                        |")
    print("                    |______________________________________|")
    
    print("\n")
    choice = int(input("                            ENTER YOUR CHOICE : "))

    t = 1
    
    if choice == 1:
        ch = listData("GAD AIR CONDITIONER.txt","A ")
        if ch != "":
            obj = a.AirConditioner()
            obj.display(ch)
    elif choice == 2:
        ch = listData("GAD HOME THEATRE.txt","H ")
        if ch != "":
            obj = h.HomeTheatre()
            obj.display(ch)
    elif choice == 3:
        ch = listData("GAD LAPTOP.txt","L ")
        if ch != "":
            obj = l.Laptop()
            obj.display(ch)
    elif choice == 4:
        ch = listData("GAD MOBILE.txt", "M ")
        if ch != "":
            obj = m.Mobile()
            obj.display(ch)
    elif choice == 5:
        ch = listData("GAD POWER BANK.txt","P ")
        if ch != "":
            obj = p.PowerBank()
            obj.display(ch)
    elif choice == 6:
        ch = listData("GAD SMART WATCH.txt","S ")
        if ch != "":
            obj = s.SmartWatch()
            obj.display(ch)
    elif choice == 7:
        ch = listData("GAD TELEVISION.txt","T ")
        if ch != "":
            obj = t.Television()
            obj.display(ch)
    elif choice == 8:
        homepage()
    else:
        t = 0
        print("")
        print("                    ****************************************")
        print("                    *          INVALID CHOICE !!!          *")
        print("                    ****************************************")
        print("\n")
        print("                           ",end = '')
        pause = input("PRESS ENTER TO CONTINUE...")
        viewDevice()
        
    if t == 1:
        print("\n")
        print("                           ",end = '')
        pause = input("PRESS ENTER TO CONTINUE...")
        viewDevice()

#Function to display and choose between options available for admin
def adminOpt():
    print("\n\n")
    print("                    ****************************************")
    print("                    *                 ADMIN                *")
    print("                    ****************************************")
    print("                    |                                      |")
    print("                    |    1. ADD DEVICE                     |")
    print("                    |                                      |")
    print("                    |    2. VIEW DEVICE                    |")
    print("                    |                                      |")
    print("                    |    3. GO BACK                        |")
    print("                    |______________________________________|")
    
    print("\n")
    choice = int(input("                            ENTER YOUR CHOICE : "))

    t = 1
    
    if choice == 1:
        addDevice()
    elif choice == 2:
        viewDevice()
    elif choice == 3:
        homepage()
    else:
        t = 0
        print("")
        print("                    ****************************************")
        print("                    *          INVALID CHOICE !!!          *")
        print("                    ****************************************")
        print("\n")
        print("                           ",end = '')
        pause = input("PRESS ENTER TO CONTINUE...")
        adminOpt()

    if t == 1:
        print("\n")
        print("                           ",end = '')
        pause = input("PRESS ENTER TO CONTINUE...")
        adminOpt()

#Function to enter admin page only if the password matches
def admin():
    print("\n\n")
    print("                    ****************************************")
    print("                    *             ADMIN ACCESS             *")
    print("                    ****************************************")
    print("\n")
    password = input("                    PASSWORD : ")

    #Comparing the entered password
    if password == "12345":
        adminOpt()
    else:
        print("\n")
        print("                    ****************************************")
        print("                    *           INVALID PASSWOORD          *")
        print("                    ****************************************")
        print("\n")
        print("                           ",end = '')
        pause = input("PRESS ENTER TO CONTINUE...")
        homepage()

#Function to choose between admin and customer
def homepage():
    print("\n\n")
    print("                    ****************************************")
    print("                    *                ACCESS                *")
    print("                    ****************************************")
    print("                    |                                      |")
    print("                    |    1. ADMIN                          |")
    print("                    |                                      |")
    print("                    |    2. CUSTOMER                       |")
    print("                    |______________________________________|")

    print("\n")
    choice = int(input("                            ENTER YOUR CHOICE : "))

    if choice == 1:
        admin()
    elif choice == 2:
        viewDevice()
    else:
        print("")
        print("                    ****************************************")
        print("                    *          INVALID CHOICE !!!          *")
        print("                    ****************************************")

    print("\n")
    print("                           ",end = '')
    pause = input("PRESS ENTER TO CONTINUE...")
    homepage()

#Main function where the program execution starts
def main():
    a = '~'

    print("\n\n\n\n\n")
    print("                    ****************************************")
    print("                    *             GADGET FINDER            *")
    print("                    ****************************************")
    print("                    |                                      |")
    print("                    |    DESIGNED BY :                     |")
    print("                    |                                      |")
    print("                    |    20PC13 - GURU PRASANNA V          |")
    print("                    |                                      |")
    print("                    |    20PC22 - NAVIN KRISHNA T          |")
    print("                    |                                      |")
    print("                    |    20PC37 - VETRIVEL M D             |")
    print("                    |______________________________________|")
    print("\n")
    print("                                   LOADING...")
    print("")
    print("                    ",end = '')

    i = 1
    while i <= 40:
        print(a,end = '')
        time.sleep(0.03)
        i = i + 1

    homepage();

main()
