import Utilities as Util

class Dimension:

     #Constructor
     def _init_(self):
          self.length = 0.0
          self.breadth = 0.0
          self.depth = 0.0

     #Function to get details related to Dimension of a particular gadget
     def getInput(self, fname):
          print("\n                                    DIMENSION\n")

          self.length = int(input("ENTER LENGTH (cm)  : "))

          self.breadth = int(input("ENTER BREADTH (cm) : "))

          self.depth = int(input( "ENTER HEIGHT (cm)  : "))

          f = open(fname, "a")

          f.write("LENGTH  : " + str(self.length) + " cm\n")
          f.write("BREADTH : " + str(self.breadth) + " cm\n")
          f.write("DEPTH   : " + str(self.depth) + " cm\n")
          f.write("\n")

          f.close()

     #Function to fetch and display Dimension details from a particular gadget
     def display(self, fname):
          print("\n                                    DIMENSION\n")

          Util.show(fname, "LENGTH  :")
