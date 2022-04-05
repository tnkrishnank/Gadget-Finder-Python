import Utilities as Util
import Electronics as Elect
import Battery as battery
import Dimension as dimension

class PowerBank(Elect.Electronics):

    #Constructor
    def _init_(self):
        self.nTypeC = 0
        self.nUsb = 0
        self.output = 0

    #Function to get details related to PowerBank
    def getInput(self):
        print("\n")
        print("********************************************************************************")
        print("*                                  POWER BANK                                  *")
        print("********************************************************************************")

        print("\n                                     GENERAL\n")

        super().getInput("P ")

        print("")

        self.nTypeC = int(input("ENTER NUMBER OF TYPE-C PORTS : "))
            
        self.nUsb = int(input("ENTER NUMBER OF USB PORTS    : "))
        
        self.output = int(input("ENTER OUTPUT (W)             : "))

        f = open(self.fname,"a")
        
        f.write("NUMBER OF TYPE-C PORTS : " + str(self.nTypeC) + "\n")
        f.write("NUMBER OF USB PORTS    : " + str(self.nUsb) + "\n")
        f.write("OUTPUT                 : " + str(self.output) + "\n")
        f.write("\n")

        f.close()

        battery.Battery.getInput(self,self.fname)
        dimension.Dimension.getInput(self,self.fname)
        
        Util.addModel("GAD POWER BANK.txt", self.model)

    #Function to fetch and display details from a particular PowerBank model
    def display(self,model):
        self.fname = "P " + model + ".txt"

        try:
            f = open(self.fname, "r")

            print("\n")
            print("********************************************************************************")
            print("*                                  POWER BANK                                  *")
            print("********************************************************************************")

            print("\n                                     GENERAL\n")

            Elect.Electronics.display(self)

            print("")
    
            Util.show(self.fname, "NUMBER OF TYPE-C PORTS :")

            battery.Battery.display(self,self.fname)
            dimension.Dimension.display(self,self.fname)
               
            f.close()
            
        except IOError:
            print("\n")
            print("********************************************************************************")
            print("*                              FILE NOT FOUND !!!                              *")
            print("********************************************************************************")
