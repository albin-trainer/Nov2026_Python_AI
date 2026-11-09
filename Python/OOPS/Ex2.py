class Account:
    def __init__(self,accNum, accHolderName,bankBalance):
        self.accNum=accNum
        self.accHolderName=accHolderName
        self.bankBalance=bankBalance

    def printAccInfo(self):
        print(f"Acc Num : {self.accNum} acc Name {self.accHolderName} Balance {self.bankBalance}")

    def fundTransfer(self,beneficiaryAccount,amtToTransfer):
        #pass ## Empty function, here u need to write the logic ....
        if self.bankBalance>=amtToTransfer :
            self.bankBalance=self.bankBalance-amtToTransfer
            a2.bankBalance=a2.bankBalance+amtToTransfer
            print("----Transaction completed----")

        else:
            print("-----Sorry insufficient Funds !!!!------")

a1= Account(123456789,"Siva",10000)
a2=Account(987654321,"Ganesh",5000)
a1.printAccInfo()
a2.printAccInfo()
a1.fundTransfer(a2,11000) # Debit from Siva's acc and credit to Ganesh account

a1.printAccInfo()
a2.printAccInfo()