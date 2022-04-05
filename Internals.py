import Utilities as Util

class Internals:

     #Constructor
     def _init_(self):
          self.ram = 0
          self.storage = 0
          self.network = ""
          self.os = ""
          self.processor = ""

     #Function to get details related to Internals of a particular gadget
     def getInput(self, fname):
          print("\n                                    INTERNALS\n")

          self.ram = int(input("ENTER RAM SIZE (GB)     : "))
          
          self.storage = int(input("ENTER STORAGE SIZE (GB) : "))

          self.network = input("ENTER NETWORK DETAILS   : ")
          self.network = self.network.upper()
          
          self.os = input("ENTER OS                : ")
          self.os = self.os.upper()

          self.processor = input("ENTER PROCESSOR DETAILS : ")
          self.processor = self.processor.upper()

          f = open(fname, "a")

          f.write("RAM SIZE          : " + str(self.ram) + " GB\n")
          f.write("STORAGE SIZE      : " + str(self.storage) + " GB\n")
          f.write("NETWORK DETAILS   : " + self.network + "\n")
          f.write("OS                : " + self.os + "\n")
          f.write("PROCESSOR DETAILS : " + self.processor + "\n")
          f.write("\n")

          f.close()

     #Function to fetch and display Internals details from a particular gadget
     def display(self,fname):
          print("\n                                    INTERNALS\n")

          Util.show(fname, "RAM SIZE          :")
