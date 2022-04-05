class Electronics:

     #Constructor
     def _init_(self):
          self.fname = ""
          self.brand = ""
          self.model = ""
          self.price = 0.0
          self.releaseYear = 0
          self.warranty = 0
          self.weight = 0
          self.colour = ""
          self.addFeatures = ""

     #Function to get common details of all gadgets
     def getInput(self, label):
          self.brand = input("ENTER BRAND               : ")
          self.brand = self.brand.upper()

          self.model = input("ENTER MODEL               : ")
          self.model = self.model.upper()

          self.price = int(input("ENTER PRICE               : Rs. "))

          self.releaseYear = int(input("ENTER RELEASE YEAR        : "))

          self.warranty = int(input( "ENTER WARRANTY (YEARS)    : "))

          self.weight = int(input("ENTER WEIGHT (kg)         : "))

          self.colour = input("ENTER COLOURS AVAILABLE   : ")
          self.colour = self.colour.upper()

          self.addFeatures = input("ENTER ADDITIONAL FEATURES : ")
          self.addFeatures = self.addFeatures.upper()

          f = open(label + self.model + ".txt", "w")
          self.fname = label + self.model + ".txt"

          f.write("BRAND               : " + self.brand + "\n")
          f.write("MODEL               : " + self.model + "\n")
          f.write("PRICE               : Rs. " + str(self.price) + "\n")
          f.write("RELEASE YEAR        : " + str(self.releaseYear) + "\n")
          f.write("WARRANTY            : " + str(self.warranty) + "\n")
          f.write("WEIGHT              : " + str(self.weight) + "\n")
          f.write("COLOURS             : " + self.colour + "\n")
          f.write("ADDITIONAL FEATURES : " + self.addFeatures + "\n")
          f.write("\n")

          f.close()

     #Function to fetch and display common details of a particular gadget
     def display(self):
          f = open(self.fname, "r")

          for x in f:
               if(x == "\n"):
                    break
               
               print(x,end = "")
