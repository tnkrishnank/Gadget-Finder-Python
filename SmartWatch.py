import Utilities as Util
import Electronics as Elect
import Battery as battery
import Dimension as dimension
import Display as disp
import Internals as internals

class SmartWatch(Elect.Electronics):

    #Constructor
    def _init_(self):
        self.shape = ""
        self.strapMaterial = ""
        self.bodyMaterial = ""
        self.waterProof = False

    #Function to get details related to SmartWatch
    def getInput(self):
        print("\n")
        print("********************************************************************************")
        print("*                                 SMART WATCH                                  *")
        print("********************************************************************************")

        print("\n                                     GENERAL\n")

        super().getInput("S ")

        print("")

        self.shape = input("ENTER SHAPE             : ")
        self.shape = self.shape.upper()
            
        self.strapMaterial = input("ENTER STRAP MATERIAL    : ")
        self.strapMaterial = self.strapMaterial.upper()
        
        self.bodyMaterial = input("ENTER BODY MATERIAL     : ")
        self.bodyMaterial = self.bodyMaterial.upper()

        ch = input("IS IT WATER PROOF (Y/N) : ")
        self.waterProof = Util.trueFalse(ch)

        f = open(self.fname,"a")
        
        f.write("SHAPE          : " + self.shape + "\n")
        f.write("STRAP MATERIAL : " + self.strapMaterial + "\n")
        f.write("BODY MATERIAL  : " + self.bodyMaterial + "\n")
        f.write("WATER PROOF    : " + Util.checkAvail(self.waterProof) + "\n")
        f.write("\n")

        f.close()

        battery.Battery.getInput(self,self.fname)
        dimension.Dimension.getInput(self,self.fname)
        disp.Display.getInput(self,self.fname)
        internals.Internals.getInput(self,self.fname)

        Util.addModel("GAD SMART WATCH.txt", self.model)

    #Function to fetch and display details from a particular SmartWatch model
    def display(self,model):
        self.fname = "S " + model + ".txt"

        try:
            f = open(self.fname, "r")

            print("\n")
            print("********************************************************************************")
            print("*                                 SMART WATCH                                  *")
            print("********************************************************************************")

            print("\n                                     GENERAL\n")

            Elect.Electronics.display(self)

            print("")
    
            Util.show(self.fname, "SHAPE          :")

            battery.Battery.display(self,self.fname)
            dimension.Dimension.display(self,self.fname)
            disp.Display.display(self,self.fname)
            internals.Internals.display(self,self.fname)
               
            f.close()
            
        except IOError:
            print("\n")
            print("********************************************************************************")
            print("*                              FILE NOT FOUND !!!                              *")
            print("********************************************************************************")
