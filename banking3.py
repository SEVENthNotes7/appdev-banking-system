import random
import math
import datetime

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
        
           
    def main(self):
        while self.userInput != 9:
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
                    self.showBestAcc()
                elif user_input == 6:
                    self.showVIPacc()
                elif user_input == 7:
                    self.removeAcc()
                elif user_input == 8:
                    self.updateAcc()
                elif user_input == 9:
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
        print(msgColors.GREEN + "5. Best Account." + msgColors.RESET)
        print(msgColors.GREEN + "6. Show VIP Account." + msgColors.RESET)
        print(msgColors.GREEN + "7. Remove Account." + msgColors.RESET)
        print(msgColors.GREEN + "8. Update Account." + msgColors.RESET)
        print(msgColors.GREEN + "9. Exit.\n" + msgColors.RESET)

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
                        for key, value in account.items():
                            if key == acc_num_key:
                                print(msgColors.GREEN + "-"*40 + msgColors.RESET)
                                print(msgColors.GREEN + " " + str(key) + ": " + msgColors.RESET + str(value))
                            else:
                                print(msgColors.GREEN + "   " + str(key) + ": " + msgColors.RESET + str(value))
                        print(msgColors.GREEN + "-"*40 + msgColors.RESET)
                        while True:
                            self.existingAccMenu()
                            self.userInput = input(msgColors.YELLOW + "Enter Trasnsaction: " + msgColors.RESET)
                            if self.userInput.isdigit():
                                user_input = int(self.userInput)
                                if user_input == 1:
                                    self.handleDeposit(accNum=account[acc_num_key])
                                elif user_input == 2:
                                    self.handleWithdraw(accNum=account[acc_num_key])
                                elif user_input == 3:
                                    self.handleTransferFund(accNum=account[acc_num_key])
                                elif user_input == 4:
                                    print( msgColors.GREEN + "Back to main menu..." + msgColors.RESET)
                                    break
                                else:
                                    print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
                            else:
                                print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
            else:
                print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
        else:
            print(msgColors.RED + "There's no Register Account..." + msgColors.RESET)
        
    def displayAllAccount(self):
        count = len(self.accountList)
        print(msgColors.GREEN + "="*40 + msgColors.RESET)
        print(msgColors.GREEN + "Display All Account." + msgColors.RESET)
        print(msgColors.GREEN + "="*40 + msgColors.RESET)
        print(msgColors.GREEN + "Total Number if Account: " + msgColors.RESET + str(count))
        if count == 0:
            print(msgColors.RED + "No Account has been registered..." + msgColors.RESET)
        elif count != 0:
            
            for data in self.accountList:
                for key, value in data.items():
                    if key == 'accNum':
                        print(msgColors.GREEN + "-"*40 + msgColors.RESET)
                        print(msgColors.GREEN + " " + str(key) + ": " + msgColors.RESET + str(value))
                    else:
                        print(msgColors.GREEN + "   " + str(key) + ": " + msgColors.RESET + str(value))
        else:
            print(msgColors.RED + "No Valid Arrays..." + msgColors.RESET)
        print(msgColors.GREEN + "="*40 + msgColors.RESET)
        
    def transactionHistory(self):
        count = len(self.transactionList)
        
        acc_num_list = {}

        if count != 0:
            for a in self.transactionList:
                acc_num = a['Created_By']
                if acc_num not in acc_num_list:
                    acc_num_list[acc_num] = {
                        'transactions': {}
                    }
                date = a['updated_at']
                if date not in acc_num_list[acc_num]['transactions']:
                    acc_num_list[acc_num]['transactions'][date] = []
                
                acc_num_list[acc_num]['transactions'][date].append({
                    'title': a['title'],
                    'balance': a['balance'],
                    'Transaction_Ammount': a['Transaction_Ammount'],
                    'Transaction_Reference': a['Transaction_Reference'],
                })
            
            sorted_acc_num = sorted(acc_num_list.keys())
            print()
            print(msgColors.GREEN + "=" * 30 + msgColors.RESET)
            print(msgColors.GREEN + "Transaction Logs" + msgColors.RESET)
            print(msgColors.GREEN + "=" * 30 + msgColors.RESET)
            for acc_num in sorted_acc_num:
                print(msgColors.GREEN + f"Account Number: " + msgColors.RESET + str(acc_num))
                details = acc_num_list[acc_num]
                for date, transactions, in details['transactions'].items():
                    print(msgColors.GREEN + "  Date: " + msgColors.RESET + str(date))
                    for transaction in transactions:
                        print(msgColors.GREEN + "   Transaciton:" + msgColors.RESET)
                        print(msgColors.GREEN + "      Title: " + msgColors.RESET + str(transaction['title']))
                        print(msgColors.GREEN + "      Amount: " + msgColors.RESET + str(transaction['Transaction_Ammount']))
                        print(msgColors.GREEN + "      Ref No.: " + msgColors.RESET + str(transaction['Transaction_Reference']))
                        print(msgColors.GREEN + "      Balance: " + msgColors.RESET + str(transaction['balance']))
                print(msgColors.GREEN + "=" * 30 + msgColors.RESET)
                print()
                
        else:
            print(msgColors.RED + "No Transaction has been save..." + msgColors.RESET)
            
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
        print(msgColors.GREEN + "3. Transfer Funds." + msgColors.RESET)
        print(msgColors.GREEN + "4. Back to Main Menu." + msgColors.RESET)
           
    def handleDeposit(self, accNum):
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
                        self.handleSaveTransaction(accNum=accNum, Title=title, transacAmm=amm_to_deposit,balance=account['balance'])
                        
        else:
            print(msgColors.RED + "Invalid Input..." + msgColors.GREEN)
    
    def handleWithdraw(self, accNum):
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
                    elif float(ammount) > float(account["balance"]):
                        print("Insufficient balance.")
                    else:
                        balance = account['balance'] 
                        newBal = float(balance) - amm_to_withdraw
                        account['balance'] = str(newBal)
                        print(msgColors.GREEN + "Ammount Successfully Withdraw..." + msgColors.RESET)
                        self.handleSaveTransaction(accNum=accNum, Title=title, transacAmm=amm_to_withdraw,balance=account['balance'])          
        else:
            print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
    
    def handleTransferFund(self, accNum):
        title = "Transfer Fund"
        acc_num_key = 'accNum'
        sender_acc_num = accNum
        
        sender_balance = 0
        fund = 0
        
        for account in self.accountList:
            if acc_num_key in account and account[acc_num_key] == str(sender_acc_num):
                sender_balance += float(account['balance'])
        
        print(title)
        reciever_acc_num = input("Enter Reciever Account number: ")
        if len(reciever_acc_num) == 6:
            # if sender_balance > 1000 and fund > 1000:
            for account in self.accountList:
                if acc_num_key in account and account[acc_num_key] == str(reciever_acc_num):
                    fund = input("Enter fund to transfer: ")
                    new_bal = float(account['balance']) + float(fund)
                    account['balance'] = str(new_bal)
                    self.handleSaveTransaction(accNum=account[acc_num_key], Title=title, transacAmm=fund ,balance=account['balance'])
                    
            for account in self.accountList:
                if acc_num_key in account and account[acc_num_key] == str(sender_acc_num):
                    new_bal = float(account['balance']) - float(fund)
                    account['balance'] = str(new_bal)
                    self.handleSaveTransaction(accNum=account[acc_num_key], Title=title, transacAmm=fund ,balance=account['balance'])
        else:
            print(msgColors.RED + "Invalid Account number..." + msgColors.RESET)
        
    def handleSaveTransaction(self, Title, transacAmm, accNum, balance):
        todays_date = datetime.date.today()
        formatted_date = todays_date.strftime("%A, %B %d, %Y")
        
        # generate transaction number
        digits = [i for i in range(0,10)]
        trans_ref = ""
        for i in range(6):
            index = math.floor(random.random()*10)
            trans_ref += str(digits[index])
        
        transaction_logs = {'title' : Title,
                            'Created_By': accNum,
                            'Transaction_Ammount': transacAmm,
                            'Transaction_Reference': trans_ref,
                            'balance': balance,
                            'updated_at': formatted_date}
        
        self.transactionList.append(transaction_logs)
        print(msgColors.GREEN + "Transaction Save..." + msgColors.RESET)
    
    def showBestAcc(self):
        count = len(self.accountList)
        sorted_balance = sorted(self.accountList, key=lambda x: x['balance'], reverse=True)
        top_3 = sorted_balance[:3]
        if count != 0:
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            print(msgColors.GREEN + "Best Account" + msgColors.RESET)
            print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            print(msgColors.GREEN + " Total Number of Account:" + msgColors.RESET + str(count))
            print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            for i, x in enumerate(top_3):
                print(msgColors.GREEN + "  Top: " + msgColors.RESET + str(i+1))
                for key, value in x.items():
                    print(msgColors.GREEN + "   " + str(key) + ": " + msgColors.RESET + str(value))
                print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
        else:
            print(msgColors.RED + "No Registered Account..." + msgColors.RESET)
        
    def showVIPacc(self):
        err_level_acc = "No Account have reach this VIP Level..."
        count = len(self.accountList)
        
        gold = []
        silver = []
        bronze = []
        
        if count != 0:
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            print(msgColors.GREEN + "VIP Account" + msgColors.RESET)
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            for i in self.accountList:
                user_blance = i['balance']
                if float(user_blance) >= 1000000:
                    acc_num = i['accNum']
                    acc_name = i['accName']
                    user_blance = i['balance']
                    acc = {
                        'accNum': acc_num,
                        'accName': acc_name,
                        'balance' : user_blance
                    }
                    gold.append(acc)
                elif float(user_blance) < 999999 and float(user_blance) > 500000:
                    acc_num = i['accNum']
                    acc_name = i['accName']
                    user_blance = i['balance']
                    acc = {
                        'accNum': acc_num,
                        'accName': acc_name,
                        'balance' : user_blance
                    }
                    silver.append(acc)
                else:
                    acc_num = i['accNum']
                    acc_name = i['accName']
                    user_blance = i['balance']
                    acc = {
                        'accNum': acc_num,
                        'accName': acc_name,
                        'balance' : user_blance
                    }
                    bronze.append(acc)
                    
            count_gold = len(gold)
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            print(msgColors.GREEN + "Gold" + msgColors.RESET)
            print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            if count_gold != 0:
                for data in gold:
                    for key, value in data.items():
                        if key == 'accNum':
                            print(msgColors.GREEN +  str(key) + ": " + msgColors.RESET + str(value))
                        else:
                            print(msgColors.GREEN +  "   " + str(key) + ": " + msgColors.RESET + str(value))
                    print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            else:
                print(msgColors.RED + err_level_acc + msgColors.RESET)
                print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            
            count_silver = len(silver)
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            print(msgColors.GREEN + "Silver" + msgColors.RESET)
            print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            if count_silver != 0:
                for data in silver:
                    for key, value in data.items():
                        if key == 'accNum':
                            print(msgColors.GREEN +  str(key) + ": " + msgColors.RESET + str(value))
                        else:
                            print(msgColors.GREEN +  "   " + str(key) + ": " + msgColors.RESET + str(value))
                    print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            else:
                print(msgColors.RED + err_level_acc + msgColors.RESET)
                print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
                    
            count_bronze = len(bronze)
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            print(msgColors.GREEN + "Bronze" + msgColors.RESET)
            print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            if count_bronze != 0:
                for data in bronze:
                    for key, value in data.items():
                        if key == 'accNum':
                            print(msgColors.GREEN +  str(key) + ": " + msgColors.RESET + str(value))
                        else:
                            print(msgColors.GREEN +  "   " + str(key) + ": " + msgColors.RESET + str(value))
                    print(msgColors.GREEN + "-" * 40 + msgColors.RESET)
            else:
                print(msgColors.RED + err_level_acc + msgColors.RESET)
                print(msgColors.GREEN + "=" * 40 + msgColors.RESET) 
            
        else: 
            print(msgColors.RED + "No Registered Account..." + msgColors.RESET)
        
    def removeAcc(self):
        acc_num_key = 'accNum'
        count = len(self.accountList)
        if count != 0:
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            print(msgColors.GREEN + "Remove Account" + msgColors.RESET)
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            user_input = input(msgColors.YELLOW + "Enter Account Number: " + msgColors.RESET)
            if user_input.isdigit():
                if len(user_input) == 6:
                    for account in self.accountList:
                        if account[acc_num_key] == user_input:
                            confirm = input(msgColors.YELLOW + "Do you want to delete this account. (Y/N): " + msgColors.RESET)
                            if confirm == 'Y' or confirm == 'y':
                                self.accountList.remove(account)
                                print(msgColors.RED + "Account successfully deleted..." + msgColors.RESET)
                            elif confirm == 'N' or confirm == 'n':
                                self.main()
                            else:
                                print(msgColors.RED + "Deleting account has been cancelled..." + msgColors.RESET)
                else:
                    print(msgColors.RED + "Invalid Account Number (must be 6 digit)" + msgColors.RESET)
            else:
                print(msgColors.RED + "Invalid Input... (input must be a 6 digit integer)" + msgColors.RESET) 
        else:
            print(msgColors.RED + "No Registerd Account found!.." + msgColors.RESET)  
        
    def updateAcc(self):
        acc_num_key = 'accNum'
        count = len(self.accountList)
        if count != 0:
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            print(msgColors.GREEN + "Update Account" + msgColors.RESET)
            print(msgColors.GREEN + "=" * 40 + msgColors.RESET)
            user_input = input(msgColors.YELLOW + "Enter Account Number: " + msgColors.RESET)
            if user_input.isdigit():
                if len(user_input) == 6:
                    for account in self.accountList:
                        if acc_num_key in account and account[acc_num_key] == str(user_input):
                            acc_num = account['accNum']
                            user_choice = input(msgColors.YELLOW + "Do you want to update this account? (Y/N):  " + msgColors.RESET)
                            if user_choice == 'Y' or user_choice == 'y':
                                self.handleUpdateAcc(accNum=acc_num)
                            elif user_choice == 'N' or user_choice == 'n':
                                self.main()
                            else:
                                print(msgColors.RED + "Invalid input.." + msgColors.RESET)
                else:
                    print(msgColors.RED + "Invalid Account Number..." + msgColors.RESET)
            else:
                print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
        else:
            print(msgColors.RED + "No Registered Account.." + msgColors.RESET)
    
    def updateAccMenu(self):
        print(msgColors.GREEN + "="*40 + msgColors.RESET)
        print(msgColors.GREEN + "Select option" + msgColors.RESET)
        print(msgColors.GREEN + "="*40 + msgColors.RESET)
        print(msgColors.GREEN + "1. Update account name." + msgColors.RESET)
        print(msgColors.GREEN + "2. Update account type." + msgColors.RESET)
        print(msgColors.GREEN + "3. Update Gender." + msgColors.RESET)
        print(msgColors.GREEN + "4. Update Address." + msgColors.RESET)
        print(msgColors.GREEN + "5. Back to Main Menu" + msgColors.RESET)
        print(msgColors.GREEN + "="*40 + msgColors.RESET)
    
    def handleUpdateAcc(self, accNum):
        title = "Update Account"
        userInput = 0
        if accNum != 0:
            for data in self.accountList:
                if data['accNum'] == accNum:
                    while userInput != 5:
                        print(msgColors.GREEN + "="*40 + msgColors.RESET)
                        print( msgColors.GREEN +  title + msgColors.RESET)
                        print(msgColors.GREEN + "="*40 + msgColors.RESET)
                        for key, value in data.items():
                            if accNum != 0:
                                if key == 'accNum':
                                    print(msgColors.GREEN +  " " + str(key) + ": " + msgColors.RESET + str(value))
                                else:
                                    print(msgColors.GREEN +  "  " + str(key) + ": " + msgColors.RESET + str(value))
                        self.updateAccMenu()
                        userInput = input(msgColors.YELLOW + "Enter your choice: " + msgColors.RESET)
                        if userInput.isdigit():
                            user_input = int(userInput)
                            if user_input == 1:
                                self.updateAccName(accNum=accNum)
                            elif user_input == 2:
                                self.updateAccType(accNum=accNum)
                            elif user_input == 3:
                                self.updateGender(accNum=accNum)
                            elif user_input == 4:
                                self.updateAddress(accNum=accNum)
                            elif user_input == 5:
                                print("Back to main menu.")
                                break
                            else:
                                print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
                        else:
                            print(msgColors.RED + "Invalid input..." + msgColors.RESET)    
    
    def updateAccName(self, accNum):
        title = "Update Account Name"
        acc_num_key = 'accNum'
        update_key = 'accName'
        print( msgColors.GREEN +  title + msgColors.RESET)
        for i in self.accountList:
            if i[acc_num_key] == accNum:
                new_acc_name = input(msgColors.YELLOW + "Enter new account name: " + msgColors.RESET)
                if not new_acc_name:
                    print(msgColors.RED + "Invalid Input..."+ msgColors.RESET)
                else:
                    if i[acc_num_key] == accNum:
                        i[update_key] = new_acc_name
                        print()
                        self.handleSaveTransaction(
                            accNum=accNum,
                            Title=title,
                            transacAmm=0,
                            balance=i['balance']
                        )
                        print()
                        self.displayAllAccount()
                        print()
                    else:
                        print(msgColors.RED + "Invalid Account number..."+ msgColors.RESET)
        
        
    def updateAccType(self, accNum):
        title = "Update accout type"
        acc_num_key = 'accNum'
        update_key = 'accType'
        print( msgColors.GREEN +  title + msgColors.RESET)
        
        for i in self.accountList:
            if i[acc_num_key] == accNum:
                new_acc_type = input(msgColors.YELLOW + "Enter New Account Type: " + msgColors.RESET)
                if not new_acc_type:
                    print(msgColors.RED + "Invalid Input..."+ msgColors.RESET)
                else:
                    if i[acc_num_key] == accNum:
                        i[update_key] = new_acc_type
                        print()
                        self.handleSaveTransaction(
                            accNum=accNum,
                            Title=title,
                            transacAmm=0,
                            balance=i['balance']
                        )
                        print()
                        self.displayAllAccount()
                        print()
                    else:
                        print(msgColors.RED + "Invalid Account Number..." + msgColors.RESET)
        
    def updateGender(self, accNum):
        title = "Update gender"
        acc_num_key = 'accNum'
        update_key = 'userGender'
        print( msgColors.GREEN +  title + msgColors.RESET)
        for i in self.accountList:
            if i[acc_num_key] == accNum:
                new_gender = input(msgColors.YELLOW + "Enter New Gender:" + msgColors.RESET)
                if not new_gender:
                    print(msgColors.RED + "Invalid input..." + msgColors.YELLOW)
                else:
                    if i[acc_num_key] == accNum:
                        i[update_key] = new_gender
                        print()
                        self.handleSaveTransaction(
                            accNum=accNum,
                            Title=title,
                            transacAmm=0,
                            balance=i['balance']
                        )
                        print()
                        self.displayAllAccount()
                        print()
                    else:
                        print(msgColors.RED + "Invalid Input..." + msgColors.YELLOW)
        
    def updateAddress(self, accNum):
        title =  "Update address"
        acc_num_key = 'accNum'
        update_key = 'userAddress'
        
        print( msgColors.GREEN +  title + msgColors.RESET)
        
        for i in self.accountList:
            if i[acc_num_key] == accNum:
                new_address = input(msgColors.YELLOW + "Enter new address: " + msgColors.RESET)
                if not new_address:
                    print(msgColors.RED + "Invalid Input..." + msgColors.RESET)
                else:
                    if i[acc_num_key] == accNum:
                        i[update_key] = new_address
                        self.handleSaveTransaction(
                            accNum=accNum,
                            Title=title,
                            transacAmm=0,
                            balance=i['balance']
                        )
                        self.displayAllAccount()
                    else:
                        print(msgColors.RED + "Invalid Input..." + msgColors.RESET)     
    
# run the program
if __name__ == "__main__":
    my_class = MyClass()
    my_class.main() 