import Utilities as Util
import Electronics as Elect
import Battery as battery
import Camera as camera
import Dimension as dimension
import Display as disp
import Internals as internals
import Ports as ports

class Laptop(Elect.Electronics):

    #Constructor
    def _init_(self):
        self.addStorage = 0
        self.touch = False
        self.graphics = False
        self.ramGraphics = 0
        self.typ = ""

    #Function to get details related to Laptop
    def getInput(self):
        print("\n")
        print("********************************************************************************")
        print("*                                    LAPTOP                                    *")
        print("********************************************************************************")

        print("\n                                     GENERAL\n")

        super().getInput("L ")

        print("")

        self.addStorage = int(input("ENTER ADDITIONAL STORAGE SIZE (GB) : "))
            
        ch = input("IS TOUCH SCREEN AVAILABLE (Y/N)    : ")
        self.touch = Util.trueFalse(ch)
        
        ch = input("IS GRAPHICS CARD AVAILABLE (Y/N)   : ")
        self.graphics = Util.trueFalse(ch)
        
        if(self.graphics):
            self.ramGraphics = int(input("ENTER GRAPHICS MEMORY SIZE (GB)    : "))
        
        self.typ = input("ENTER LAPTOP TYPE                  : ")
        self.typ = self.typ.upper()
        
        f = open(self.fname,"a")
        
        f.write("ADDITIONAL STORAGE   : " + str(self.addStorage) + " GB\n")
        f.write("TOUCH SCREEN         : " + str(self.touch) + "\n")
        
        if(self.graphics):
            f.write("GRAPHICS MEMORY SIZE : " + str(self.ramGraphics) + " GB\n")
        else:
            f.write("GRAPHICS CARD        : " + Util.checkAvail(self.graphics) + "\n")
        
        f.write("TYPE                 : " + self.typ + "\n")
        f.write("\n")

        f.close()

        battery.Battery.getInput(self,self.fname)
        camera.Camera.getInput(self,self.fname)
        dimension.Dimension.getInput(self,self.fname)
        disp.Display.getInput(self,self.fname)
        internals.Internals.getInput(self,self.fname)
        ports.Ports.getInput(self,self.fname)
        
        Util.addModel("GAD POWER BANK.txt", self.model)

    #Function to fetch and display details from a particular Laptop model
    def display(self,model):
        self.fname = "L " + model + ".txt"

        try:
            f = open(self.fname, "r")

            print("\n")
            print("********************************************************************************")
            print("*                                    LAPTOP                                    *")
            print("********************************************************************************")

            print("\n                                     GENERAL\n")

            Elect.Electronics.display(self)

            print("")
    
            Util.show(self.fname, "ADDITIONAL STORAGE   :")

            battery.Battery.display(self,self.fname)
            camera.Camera.display(self,self.fname)
            dimension.Dimension.display(self,self.fname)
            disp.Display.display(self,self.fname)
            internals.Internals.display(self,self.fname)
            ports.Ports.display(self,self.fname)
        
            f.close()
            
        except IOError:
            print("\n")
            print("********************************************************************************")
            print("*                              FILE NOT FOUND !!!                              *")
            print("********************************************************************************")
