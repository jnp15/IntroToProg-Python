#------------------------------------------------------------------
#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  Sept 16, 2017
# ChangeLog: (Who, When, What)
#   JPatten, 03/1/2019, This uses classes to add data to a table
#------------------------------------------------------------------

class Person(object):
    #Fields
    strName = ""

    #constructor
    def __init__(self,Name):
      #Attributes
      self.__Name = Name

    #properties
    #Name
    @property  # getter(accessor)
    def Name(self):
      return self.__Name

    @Name.setter #(mutator)
    def Name(self, Value):
      self.__Name = Value

    #Method
    def ToString(self):
      return str(self.Name)

    def __str__(self):
     return self.ToString()
# End of class

class Customer(Person):
    #--Fields--
    #intID = 0
    #strEmail = ""

    #--Constructor--
    def __init__(self, ID, Name, Email):
      #Attributes
      self.__ID = ID
      super(Customer, self).__init__(Name)
      self.__Email = Email

    #Properties
    # Name
    @property  #getter(accessor)
    def ID(self):
      return self.__ID

    @ID.setter  #(mutator)
    def ID(self, Value):
      self.__ID = Value

    #Name
    @property #getter(accessor)
    def Email(self):
      return self.__Email

    @Email.setter #(mutator)
    def Email(self, Value):
      self.__Email = Value

    #Methods
    def ToString(self):
      return str(self.ID) + "," + self.Name + "," + self.Email

    def __str__(self):
      return self.ToString()
#End of Class

class CustomerSaver(object):
    def SaveCustomerDataToFile(self):
        objF = open("Assignment8Data.txt", 'a')
        strAllText = ""
        for item in lstTable:
            strData = item.ToString() + "\r\n"
            strAllText += strData
            objF.write(strData)
        objF.close()
        print("The following  data was saved to a file:\n\r", strAllText)
#End of Class

class CustomError(Exception):
      def inputNumber(message):
          while True:
              try:
                  userInput = int(input(message))
              except ValueError:
                  print("Must be an integer! Try again.")
                  continue
              else:
                  return userInput
                  break
#End of Class

#1) Create dictionary  of data:
objC1 = Customer(1, "James Bond", "JBond@hotmail.com")
objC2 = Customer(2, "James Bond", "JBond@hotmail.com")
objC3 = Customer(3, "James Bond", "JBond@hotmail.com")
lstTable = [objC1,objC2,objC3]
#print(objC1)
#lstTable = []

#Add code to let user append data
#Add loop that lets the user keep adding data
while (True):
  intID = CustomError.inputNumber("Enter an ID: ")
  strName = input("Enter a name: ")
  strEmail = input("Enter an Email: ")
  objC = Customer(intID,strName,strEmail)
  lstTable.append(objC)
  if(input("Type 'exit' to end: ").lower()  == "exit"): break

#4) Ask user if they want to save data to file when they exit the loop
strSaveToFile = input("Would you like to save your entries to a file? (y/n): ")

#5 Save data to file if they say Yes
if(strSaveToFile.lower() == 'y'):
  CustomerSaver.SaveCustomerDataToFile(strSaveToFile)
else:
  print("Data has not been saved!")