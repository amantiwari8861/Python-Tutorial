class Ticket:
    passengers={}

    def booking(self):
        details={}
        print("------Enter Details For Ticket Booking-----")
        mobNo=int(input("enter the mobile No.  :"))
        details['name']=input("enter the name :")
        details['source']=input("enter the source :")
        details['destination']=input("enter the destination :")
        self.passengers[mobNo]=details
        # print(self.passengers)
    
    def print(self):
        i=0
        print("\n -------printing All Passengers List--------\n")
        for e in self.passengers:
            i+=1
            print("------------Passenger ",i," Details-----------------")
            print("Mobile No is :",e)
            # print(self.passengers[e])
            for k,v in self.passengers[e].items():
                print(k,":",v)

    def status(self):
        print("-------Check Status---------------")
        mobNo=int(input("Enter mobile No. :"))
        if self.passengers.keys().__contains__(mobNo) :
            print("ur ticket is confirmed ")
        else :
            print("ur ticket is not confirmed")


p1=Ticket()
p1.booking()
# p1.booking()
p1.status()
p1.print()