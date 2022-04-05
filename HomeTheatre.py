import Utilities as Util
import Electronics as Elect
import Dimension as dimension

class HomeTheatre(Elect.Electronics):

    #Constructor
    def _init_(self):
        self.channel = 0.0
        self.nSpeaker = 0
        self.output = 0

    #Function to get details related to HomeTheatre
    def getInput(self):
        print("\n")
        print("********************************************************************************")
        print("*                                  HOME THEATRE                                *")
        print("********************************************************************************")

        print("\n                                     GENERAL\n")

        super().getInput("H ")

        print("")

        self.channel = float(input("ENTER CHANNEL            : "))
            
        self.nSpeaker = int(input("ENTER NUMBER OF SPEAKERS : "))
        
        self.output = int(input("ENTER OUTPUT (W)         : "))

        f = open(self.fname,"a")
        
        f.write("CHANNEL            : " + str(self.channel) + "\n")
        f.write("NUMBER OF SPEAKERS : " + str(self.nSpeaker) + "\n")
        f.write("OUTPUT             : " + str(self.output) + "\n")
        f.write("\n")

        f.close()

        dimension.Dimension.getInput(self,self.fname)

        Util.addModel("GAD HOME THEATRE.txt", self.model)

    #Function to fetch and display details from a particular HomeTheatre model
    def display(self,model):
        self.fname = "H " + model + ".txt"

        try:
            f = open(self.fname, "r")

            print("\n")
            print("********************************************************************************")
            print("*                                  HOME THEATRE                                *")
            print("********************************************************************************")

            print("\n                                     GENERAL\n")

            Elect.Electronics.display(self)

            print("")
    
            Util.show(self.fname, "CHANNEL            :")

            dimension.Dimension.display(self,self.fname)
                           
            f.close()
            
        except IOError:
            print("\n")
            print("********************************************************************************")
            print("*                              FILE NOT FOUND !!!                              *")
            print("********************************************************************************")
