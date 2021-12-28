import random
class ATM(object):
    def __init__(self, cardNumber, pin, bal):
        self.cardNumber=cardNumber
        self.pin=pin
        self.bal=bal

    def withdrawCash(self,cash):
        print("Taken out ₹"+str(cash))
        currentBal=self.bal-cash
        print("Now your Balance is ₹"+currentBal)
    
    def depositCash(self,cash):
        print("Deposited ₹"+str(cash))
        currentBal=self.bal+cash
        print("Now your Balance is ₹"+currentBal)

atm=ATM(1234567890, 49311 , 10000)
task=input("Do you want to Deposit or Withdraw?").lower().strip()
cash=int(input("How much?"))
if task=="deposit":
    print("Deposite")
    atm.depositCash(cash)
if task=="withdraw":
    print("withdraw")
    atm.withdrawCash(cash)
