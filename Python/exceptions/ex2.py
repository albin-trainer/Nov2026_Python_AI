class InSufficientFunds (BaseException):
    pass


print("-----Banking App-----")
balance_amt=5000
fund_transfer=int(input("Enter the amount :"))
if balance_amt >= fund_transfer:
    balance_amt-=fund_transfer
    print(f"Successfully Transfered the Amount and the bal amt is {balance_amt}")
else:
    raise InSufficientFunds()

