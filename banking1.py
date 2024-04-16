import random

account = []
transaction = []

balance = 0

choice = 0

class main:
    def __init__(self, accName, accType, gender, address, balance):
        self.accName = accName
        self.accType = accType
        self.gender = gender
        self.address = address
        self.balance = balance

    def createAccount():
        print("Create Account.")
        accName = input("Enter Account Name:")
        accType = input("Enter Account Type:")
        gender = input("Enter Gender:")
        address = input("Enter Address:")
    
        data = main(str(accName), str(accType), str(gender), str(address), str(balance))
    
        account.append(data)
    
def existingAccount():
    print("Use Existing Account.")
    
def displayAllAccount():
    print(account);
    
def transactionHistory():   
    print("Transaction History")


while choice !=5:
    print("Banking System-Python\nEnter Your Choice\n1. Create Account\n2. Use Existing Account\n3. Display All Accounts\n4. Transaction\n5. Exit.\n")
    
    choice = int(input())
    
    if choice <0 or choice >6:
        print("\n=================\n= Invalid Input =\n=================\n")
    else:
        match choice:
            case 1:
                createAccount()
            case 2:
                existingAccount()
            case 3:
                displayAllAccount()
            case 4:
                transactionHistory()
            case 5:
                print("Program Close...\n")
            