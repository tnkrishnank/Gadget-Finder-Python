import Utilities as Util

class Camera:

     #Constructor
     def _init_(self):
          self.nCamera = 0
          self.specs = ""

     #Function to get details related to Camera of a particular gadget
     def getInput(self, fname):
          print("\n                                     CAMERA\n")

          self.nCamera = int(input("ENTER NUMBER OF CAMERAS    : "))

          self.specs = input("ENTER CAMERA SPECIFICATION : ")
          self.specs = self.specs.upper()
          
          f = open(fname, "a")

          f.write("NUMBER OF CAMERAS : " + str(self.nCamera) + "\n")
          f.write("SPECIFICATIONS    : " + str(self.specs) + "\n")
          f.write("\n")

          f.close()

     #Function to fetch and display Camera details from a particular gadget
     def display(self, fname):
          print("\n                                     CAMERA\n")
          
          Util.show(fname,"NUMBER OF CAMERAS :")
