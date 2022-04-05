#Function to return true or false based on input character
def trueFalse(ch):
     if(ch == 'y' or ch == 'Y'):
          return True

     return False

#Function to return Availability based on input
def checkAvail(chk):
     if(chk):
          return "AVAILABLE"

     return "NOT AVAILABLE"

#Function to add model number to the gadget file
def addModel(fname, model):
     f = open(fname, "a")
     f.write(model + "\n")
     f.close()

#Function to print a selected set of block
def show(fname, s):
     i = 1
    
     f = open(fname, "r")
     
     for x in f:
          if(i != 1 and x == "\n"):
               break

          if(not(x.find(s))):
               i = i + 1

          if(i > 1):
               print(x, end = "")

     f.close()
