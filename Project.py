import random
class ATM(object):
    def __init__(self, cardNumber, pin, bal):
        self.cardNumber=cardNumber
        self.pin=pin
        self.bal=bal

    def withdrawCash(self,cash):
        print("Taken out ₹"+cash)
        currentBal=int(self.bal-cash)

    def depositCash(self,cash):
        print("Deposited ₹"+cash)
        currentBal=int(self.bal+cash)


atm=ATM(10000, 1234567890, 49311)
task=input("Do you want to Deposit or Withdraw?").lower().strip()
cash=input("How much?")
if task=="deposit":
    atm.depositCash(cash)
if task=="withdraw":
    atm.withdrawCash(cash)