import Utilities as Util

class Display:

     #Constructor
     def _init_(self):
          self.displaySize = 0.0
          self.displayType = ""
          self.resHeight = 0
          self.resWidth = 0
          self.refreshRate = 0
          self.ppi = 0

     #Function to get details related to Display of a particular gadget
     def getInput(self, fname):
          print("\n                                     DISPLAY\n")

          self.displaySize = float(input("ENTER DISPLAY SIZE (inch) : "))

          self.displayType = input("ENTER DISPLAY TYPE        : ")
          self.displayType = self.displayType.upper()
          
          self.resHeight = int(input("ENTER HEIGHT RESOLUTION   : "))
          
          self.resWidth = int(input("ENTER WIDTH RESOLUTION    : "))
          
          self.refreshRate = int(input("ENTER REFRESH RATE (Hz)   : "))
          
          self.ppi = float(input("ENTER PIXEL DENSITY (ppi) : "))

          f = open(fname, "a")

          f.write("SIZE          : " + str(self.displaySize) + " inch\n")
          f.write("TYPE          : " + self.displayType + "\n")
          f.write("RESOLUTION    : " + str(self.resHeight) + " x " + str(self.resWidth) + "\n")
          f.write("REFRESH RATE  : " + str(self.refreshRate) + " Hz\n")
          f.write("PIXEL DENSITY : " + str(self.ppi) + " ppi\n")
          f.write("\n")

          f.close()

     #Function to fetch and display Display details from a particular gadget
     def display(self, fname):
          print("\n                                     DISPLAY\n")
          
          Util.show(fname, "SIZE          :")
