from random import randint

passengers={}

class Ticket:
    def generatePnr(self):
        temppnr=randint(000000,999999)
        if(passengers.__contains__(temppnr)):
            generatePnr(self)
        else:
            self.pnr=temppnr
        return self.pnr
    
    def checkPnr(self,pnr):
        if passengers.__contains__(pnr):
            print(" Your Ticket is confirmed")
            t1=passengers[pnr]
            print("Name :",t1.name)
            print("Mobile no. :",t1.mobNo)
            print("Source :",t1.source)
            print("Destination :",t1.destination)
        else:
            print("Ur ticket details is not Available")
        

class Passenger:
    def bookTicket(self):
        t=Ticket()
        print("------Enter Details For Ticket Booking-----")
        t.mobNo=int(input("enter the mobile No.  :"))
        t.name=input("enter the name :")
        t.source=input("enter the source :")
        t.destination=input("enter the destination :")
        print("ticked confirmed ! ur pnr is ",t.generatePnr())
        passengers[t.pnr]=t

p1=Passenger()
p1.bookTicket()
# p2=Passenger()
# p2.bookTicket()

T=Ticket()
T.checkPnr(int(input("enter pnr :")))

# print(passengers)

# for e in passengers:
#     print("Passenger Details ")
#     ticket=passengers[e]
#     print(ticket.mobNo)
#     print(ticket.name)
#     print(ticket.source)
#     print(ticket.destination)
