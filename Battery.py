import Utilities as Util

class Battery:

     #Constructor
     def _init_(self):
          self.capacity = 0
          self.standbyTime = 0
          self.chargerOP = 0

     #Function to get details related to Battery of a particular gadget
     def getInput(self, fname):
          print("\n                                     BATTERY\n")

          self.capacity = int(input("ENTER BATTERY CAPACITY (mAh) : "))

          self.standbyTime = int(input("ENTER STANDBY TIME (HRS)     : "))

          self.chargerOP = int(input( "ENTER CHARGER OUTPUT (W)     : "))

          f = open(fname, "a")

          f.write("CAPACITY       : " + str(self.capacity) + " mAh\n")
          f.write("STANDBY TIME   : " + str(self.standbyTime) + " HRS\n")
          f.write("CHARGER OUTPUT : " + str(self.chargerOP) + " W\n")
          f.write("\n")

          f.close()

     #Function to fetch and display Battery details from a particular gadget
     def display(self, fname):
          print("\n                                     BATTERY\n")

          Util.show(fname,"CAPACITY       :")
