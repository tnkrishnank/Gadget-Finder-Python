import Utilities as Util
import Electronics as Elect
import Dimension as dimension
import Display as disp
import Internals as internals
import Ports as ports

class Television(Elect.Electronics):

     #Constructor
     def _init_(self):
          self.typ = 1

     #Function to get details related to Television
     def getInput(self):
          print("\n")
          print("********************************************************************************")
          print("*                                  TELEVISION                                  *")
          print("********************************************************************************")

          print("\n                                     GENERAL\n")

          super().getInput("T ")

          print("")

          print("TYPES      : 1. SMART TV")
          print("             2. ANDROID TV")
          
          self.typ = int(input("ENTER TYPE : "))

          if(self.typ == 2):
               ch = "ANDROID TV"
          else:
               self.typ = 1
               ch = "SMART TV"

          f = open(self.fname, "a")
          
          f.write("TYPE : " + ch + "\n")
          f.write("\n")
          
          f.close()

          dimension.Dimension.getInput(self,self.fname)
          disp.Display.getInput(self,self.fname)

          if(self.typ == 2):
               internals.Internals.getInput(self,self.fname)

          ports.Ports.getInput(self,self.fname)

          Util.addModel("GAD TELEVISION.txt", self.model)

     #Function to fetch and display details from a particular Television model
     def display(self,model):
          i = 1
          ch = ""
          self.fname = "T " + model + ".txt"
          
          try:
               f = open(self.fname, "r")

               print("\n")
               print("********************************************************************************")
               print("*                                  TELEVISION                                  *")
               print("********************************************************************************")

               print("\n                                     GENERAL\n")

               Elect.Electronics.display(self)

               print("")

               Util.show(self.fname,"TYPE :")

               for x in f:
                    if(i != 1 and x == "\n"):
                         break

                    if(x == "TYPE : ANDROID TV\n"):
                         i = i + 1

                    if(i > 1):
                         ch = x

               dimension.Dimension.display(self,self.fname)
               disp.Display.display(self,self.fname)

               if(ch == "TYPE : ANDROID TV\n"):
                    internals.Internals.display(self,self.fname)

               ports.Ports.display(self, self.fname)

               f.close()
               
          except IOError:
               print("\n")
               print("********************************************************************************")
               print("*                              FILE NOT FOUND !!!                              *")
               print("********************************************************************************")
