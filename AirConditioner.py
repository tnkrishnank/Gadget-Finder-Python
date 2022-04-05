import Utilities as Util
import Electronics as Elect
import Dimension as dimension

class AirConditioner(Elect.Electronics):

    #Constructor
    def _init_(self):
        self.tonnage = 0.0
        self.area = 0.0
        self.energyRating = 0
        self.compressorType = ""
        self.typ = ""

    #Function to get details related to AirConditioner
    def getInput(self):
        print("\n")
        print("********************************************************************************")
        print("*                                AIR CONDITIONER                               *")
        print("********************************************************************************")

        print("\n                                     GENERAL\n")

        super().getInput("A ")

        print("")
          
        self.tonnage = int(input("ENTER TONNAGE           : "))
          
        self.area = int(input("ENTER AREA (SQ. FEETS)  : "))
          
        self.energyRating = int(input("ENTER ENERGY RATING     : "))
          
        self.compressorType = input("ENTER COMPRESSOR TYPE   : ")
        self.compressorType = self.compressorType.upper()
          
        self.typ = input("ENTER AC TYPE           : ")
        self.typ = self.typ.upper()

        f = open(self.fname, "a")
          
        f.write("TONNAGE           : " + str(self.tonnage) + "\n")
        f.write("AREA              : " + str(self.area) + "\n")
        f.write("ENERGY RATING     : " + str(self.energyRating) + "\n")
        f.write("COMPRESSOR TYPE   : " + self.compressorType + "\n")
        f.write("AC TYPE           : " + self.typ + "\n")
        f.write("\n")
          
        f.close()

        dimension.Dimension.getInput(self,self.fname)

        Util.addModel("GAD AIR CONDITIONER.txt", self.model)

    #Function to fetch and display details from a particular AirConditioner model
    def display(self,model):
        self.fname = "A " + model + ".txt"

        try:
            f = open(self.fname, "r")

            print("\n")
            print("********************************************************************************")
            print("*                                AIR CONDITIONER                               *")
            print("********************************************************************************")

            print("\n                                     GENERAL\n")

            Elect.Electronics.display(self)
            
            print("")
    
            Util.show(self.fname, "TONNAGE           :")

            dimension.Dimension.display(self,self.fname)
               
            f.close()
               
        except IOError:
            print("\n")
            print("********************************************************************************")
            print("*                              FILE NOT FOUND !!!                              *")
            print("********************************************************************************")
