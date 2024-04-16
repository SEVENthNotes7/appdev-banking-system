import random
import math
from datetime import datetime

class msgColors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

class MyClass:
    def __init__(self):
        self.userInput = 0
        self.accountList = []
        self.transactionList = []
        
        self.date = datetime.now()
           
    def main(self):
        while self.userInput != 5:
            self.mainMenu()
            self.userInput = input(msgColors.YELLOW + "Enter Your choise: " + msgColors.RESET)
            if self.userInput.isdigit():
                user_input = int(self.userInput)
                if user_input == 1:
                    self.createAccount()
                elif user_input == 2:
                    self.useExistingAccount()
                elif user_input == 3:
                    self.displayAllAccount()
                elif user_input == 4:
                    self.transactionHistory()
                elif user_input == 5:
                    print(msgColors.RED + "Closing the program..." + msgColors.RESET)
                    break
                else:
                    print(msgColors.RED + "Invalid input please try again..." + msgColors.RESET)
            else:
                print(msgColors.RED + "Invalid input..." + msgColors.RESET)
            
    def mainMenu(self):
        print(msgColors.GREEN + "\nBanking System - Python\n" + msgColors.RESET)
        print(msgColors.GREEN + "1. Create Account." + msgColors.RESET)
        print(msgColors.GREEN + "2. Use Existing Account." + msgColors.RESET)
        print(msgColors.GREEN + "3. Display All Accounts." + msgColors.RESET)
        print(msgColors.GREEN + "4. Transaction History." + msgColors.RESET)
        print(msgColors.GREEN + "5. Exit.\n" + msgColors.RESET)

    def createAccount(self):
        print(msgColors.GREEN + "Create Account.")
        accName = input(msgColors.YELLOW + "Enter Account Name:" + msgColors.RESET)
        accType = input(msgColors.YELLOW + "Enter Account Type:" + msgColors.RESET)
        Gender = input(msgColors.YELLOW + "Enter User Gender:" + msgColors.RESET)
        Address = input(msgColors.YELLOW + "Enter User Address:" + msgColors.RESET)
        self.handleCreateAccount(accName=accName, accType=accType, userGender=Gender, userAddress=Address)
    
    def useExistingAccount(self):
        acc_num_key = 'accNum'
        count = len(self.accountList)
        if count != 0:
            print(msgColors.GREEN + "Use Existing Account." + msgColors.RESET)
            acc_num = input(msgColors.YELLOW + "Enter account number: " + msgColors.RESET)
            if acc_num.isdigit():
                for account in self.accountList:
                    if acc_num_key in account and account[acc_num_key] == str(acc_num):
                        print(msgColors.GREEN + "Successfully Login" + msgColors.RESET)
                        print(
                            " Account Number:", account[acc_num_key], "Account Name:", account['accName'], "Account Type:", account['accType'], "User Gender:", account['userGender'], "User Address:", account['userAddress'], "Balance:", account['balance'],
                        )
                        while True:
                            self.existingAccMenu()
                            self.userInput = input(msgColors.YELLOW + "Enter Trasnsaction: " + msgColors.RESET)
                            if self.userInput.isdigit():
                                user_input = int(self.userInput)
                                if user_input == 1:
                                    self.handleDeposit(accNum=account[acc_num_key], accName=account['accName'])
                                elif user_input == 2:
                                    self.handleWithdraw(accNum=account[acc_num_key], accName=account['accName'])
                                elif user_input == 3:
                                    print( msgColors.GREEN + "Back to main menu..." + msgColors.RESET)
                                    break
            else:
                print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
        else:
            print(msgColors.RED + "There's no Register Account..." + msgColors.RESET)
        
    def displayAllAccount(self):
        
        count = len(self.accountList)
        
        if count == 0:
            print(msgColors.RED + "No Account has been registered..." + msgColors.RESET)
        elif count != 0:
            print(msgColors.GREEN + "Display All Account." + msgColors.RESET)
            for i in self.accountList:
                print(" Account Number:", i['accNum']," Account Name:", i['accName']," Account Type:", i['accType']," User Gender:", i['userGender']," User Address:", i['userAddress']," Balance:", i['balance'],
                    )
        else:
            print(msgColors.RED + "No Valid Arrays..." + msgColors.RESET)
            
    def transactionHistory(self):
        count = len(self.transactionList)
        
        if count == 0:
            print(msgColors.RED + "No Transaction has been save..." + msgColors.RESET)
        elif count != 0:
            print(msgColors.GREEN + "Transaction History." + msgColors.RESET)
            for i in self.transactionList:
                print(" Title:", i['Title']," Transaction Ammount:", i['Transaction_Ammount']," Transaction Reference:", i['Transaction_Reference']," Created By:", i['Created_By']," Balance:", i['balance']," Date Updated:", i['updated_at']
                )
        else:
            print(msgColors.RED + "No Valid Arrays..." + msgColors.RESET )
            
    def handleCreateAccount(self, accName, accType, userGender, userAddress):
        
        balance = 0

        # generate user id using random and math
        digits = [i for i in range(0,10)]
        accNum = ""
        for i in range(6):
            index = math.floor(random.random()*10)
            accNum += str(digits[index])
        
        self.accountList.append({'accNum': accNum,'accName':accName,'accType':accType,'userGender':userGender,'userAddress':userAddress,'balance':str(balance)} )
        
        print(msgColors.GREEN + "Account Successfully Created!.." + msgColors.RESET)
        
    def existingAccMenu(self):
        print(msgColors.GREEN + "Chose Transaction." + msgColors.RESET)
        print(msgColors.GREEN + "1. Deposit." + msgColors.RESET)
        print(msgColors.GREEN + "2. Withdraw." + msgColors.RESET)
        print(msgColors.GREEN + "3. Back to Main Menu." + msgColors.RESET)
           
    def handleDeposit(self, accNum, accName):
        title = "Deposit"
        print(msgColors.GREEN + title + msgColors.RESET)
        acc_num_key = 'accNum'
        amount = input(msgColors.YELLOW + "Enter Amount To Deposit: " + msgColors.RESET)
        if amount.isdigit():
            amm_to_deposit = float(amount)
            if amm_to_deposit < 1000:
                print(msgColors.RED + "You can not deposit any amount less than 1000" + msgColors.RESET)
            else:
                for account in self.accountList:
                    if acc_num_key in account and account[acc_num_key] == accNum:
                        balance = account['balance']
                        newBal = float(balance) + amm_to_deposit
                        account['balance'] = str(newBal)
                        print(msgColors.GREEN + "Ammount Successfully deposited..." + msgColors.RESET)
                        self.handleSaveTransaction(accName=accName, Title=title, transacAmm=amm_to_deposit,balance=account['balance'])
                        
        else:
            print(msgColors.RED + "Invalid Input..." + msgColors.GREEN)
    
    def handleWithdraw(self, accNum, accName):
        title = "Withdraw"
        print(msgColors.GREEN + title + msgColors.RESET)
        acc_num_key = 'accNum'
        ammount = input(msgColors.YELLOW + "Enter Ammount to withdraw: " + msgColors.RESET)
        
        if ammount.isdigit():
            amm_to_withdraw = float(ammount)
            for account in self.accountList:
                if acc_num_key in account and account[acc_num_key] == accNum:
                    if float(account['balance']) <= 1000:
                        print(msgColors.RED + "You can't withdraw if your balance is less than 1000" + msgColors.RESET)
                    else:
                        balance = account['balance'] 
                        newBal = float(balance) - amm_to_withdraw
                        account['balance'] = str(newBal)
                        print(msgColors.GREEN + "Ammount Successfully Withdraw..." + msgColors.RESET)
                        self.handleSaveTransaction(accName=accName, Title=title, transacAmm=amm_to_withdraw,balance=account['balance'])          
        else:
            print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
        
    def handleSaveTransaction(self, Title, transacAmm, accName, balance):
        date = str(self.date)
        
        # generate transaction number
        digits = [i for i in range(0,10)]
        trans_ref = ""
        for i in range(6):
            index = math.floor(random.random()*10)
            trans_ref += str(digits[index])
            
        self.transactionList.append({'Title' : Title,'Transaction_Ammount': transacAmm,'Transaction_Reference': trans_ref,'Created_By': accName,'balance': balance,'updated_at': date})
        print("Transaction Save...")
        
        
if __name__ == "__main__":
    my_class = MyClass()
    my_class.main() 