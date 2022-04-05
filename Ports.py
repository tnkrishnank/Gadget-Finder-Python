import Utilities as Util

class Ports:

     #Constructor
     def _init_(self):
          self.aux = False
          self.hdmi = False
          self.rj45 = False
          self.vga = False
          self.usb = False
          self.typeC = False
          self.nHdmi = 0
          self.nUsb = 0

     #Function to get details related to Ports of a particular gadget
     def getInput(self, fname):
          print("\n                                      PORTS\n")

          ch = input("IS AUX PORT AVAILABLE (Y/N)    : ")
          self.aux = Util.trueFalse(ch)
          
          ch = input("IS HDMI PORT AVAILABLE (Y/N)   : ")
          self.hdmi = Util.trueFalse(ch)

          if(self.hdmi):
               self.nHdmi = int(input("ENTER NUMBER OF HDMI PORTS     : "))
               
          ch = input("IS RJ45 PORT AVAILABLE (Y/N)   : ")
          self.rj45 = Util.trueFalse(ch)
          
          ch = input("IS VGA PORT AVAILABLE (Y/N)    : ")
          self.vga = Util.trueFalse(ch)
          
          ch = input("IS USB PORT AVAILABLE (Y/N)    : ")
          self.usb = Util.trueFalse(ch)

          if(self.usb):
               self.nUsb = int(input("ENTER NUMBER OF USB PORTS      : "))
               
          ch = input("IS TYPE-C PORT AVAILABLE (Y/N) : ")
          self.typeC = Util.trueFalse(ch)
          
          f = open(fname, "a")
          f.write("AUX                  : " + Util.checkAvail(self.aux) + "\n")

          if(self.hdmi):
               f.write("NUMBER OF HDMI PORTS : " + str(self.nHdmi) + "\n")
          else:
               f.write("HDMI                 : "+ Util.checkAvail(self.hdmi) + "\n")
               
          f.write("RJ45                 : " + Util.checkAvail(self.rj45) + "\n")
          f.write("VGA                  : " + Util.checkAvail(self.vga) + "\n")

          if(self.usb):
               f.write("NUMBER OF USB PORTS  : "+ str(self.nUsb) + "\n")
          else:
               f.write("USB                  : " + Util.checkAvail(self.usb) + "\n")

          f.write("TYPE-C               : " + Util.checkAvail(self.typeC) + "\n")
          f.write("\n")

          f.close()

     #Function to fetch and display Ports details from a particular gadget
     def display(self, fname):
          print("\n                                      PORTS\n")

          Util.show(fname, "AUX                  :")
