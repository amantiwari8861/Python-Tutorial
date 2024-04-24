class HR:
    def __init__(self):
        self.name="Aman" #public member
        self._hrId=113114 #protected member
        self.__creditCard=12345678 #private member

class Emp(HR):
    def showHrDetails(self):
       print("Hr name in showHrDetails :",self.name)
       print("Hr hrId in showHrDetails :",self._hrId)
    #    print("Hr creditCard in showHrDetails :",self.__creditCard) #private data inaccessible
       print("Hr creditCard in showHrDetails :",self._HR__creditCard) #private data inaccessible
        
obj=Emp()
obj.showHrDetails()

print(" HrId =",obj._hrId," outside the child body")  #works Fine
# print(" HrCreditCard =",obj.__creditCard," outside the child body")  #error
print(" HrCreditCard =",obj._HR__creditCard," outside the child body")  

h=HR()
print("calling private data ",h.__creditCard)
print("calling private data ",h._HR__creditCard)

# The members of a class that are declared protected are only accessible 
# to a class derived from it. Data members of a class are declared protected
#  by adding a single underscore ‘_’ symbol before the data member of that class. 

# There isn't truly private in python. This is probably considered evil.