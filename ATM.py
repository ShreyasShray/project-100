class ATM(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def CashWithdrawl(self):
        print("Cash Withdrawl")

    def BalanceEnquiry(self):
        print("Balance Enquiry")

    def CashDeposit(self):
        print("Cash Deposit")

    def ChangePin(self):
        print("Change Pin")

atm = ATM("1234-5678-0987-6642", "2606")

atm.CashDeposit()
atm.CashWithdrawl()
atm.BalanceEnquiry()
atm.ChangePin()