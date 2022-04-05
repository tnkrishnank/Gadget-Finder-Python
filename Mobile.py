import Utilities as Util
import Electronics as Elect
import Battery as battery
import Camera as camera
import Dimension as dimension
import Display as disp
import Internals as internals

class Mobile(Elect.Electronics):

    #Constructor
    def _init_(self):
        pass

    #Function to get details related to Mobile
    def getInput(self):
        print("\n")
        print("********************************************************************************")
        print("*                                    MOBILE                                    *")
        print("********************************************************************************")

        print("\n                                     GENERAL\n")

        super().getInput("M ")

        print("")

        battery.Battery.getInput(self,self.fname)
        camera.Camera.getInput(self,self.fname)
        dimension.Dimension.getInput(self,self.fname)
        disp.Display.getInput(self,self.fname)
        internals.Internals.getInput(self, self.fname)
        
        Util.addModel("GAD MOBILE.txt", self.model)

    #Function to fetch and display details from a particular Mobile model
    def display(self,model):
        self.fname = "M " + model + ".txt"

        try:
            f = open(self.fname, "r")

            print("\n")
            print("********************************************************************************")
            print("*                                    MOBILE                                    *")
            print("********************************************************************************")

            print("\n                                     GENERAL\n")

            Elect.Electronics.display(self)

            print("")

            battery.Battery.display(self,self.fname)
            camera.Camera.display(self,self.fname)
            dimension.Dimension.display(self,self.fname)
            disp.Display.display(self,self.fname)
            internals.Internals.display(self,self.fname)
            
            f.close()
            
        except IOError:
            print("\n")
            print("********************************************************************************")
            print("*                              FILE NOT FOUND !!!                              *")
            print("********************************************************************************")
