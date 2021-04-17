#Mock up ATM Project Improvements
#Login
#Register
#Bank Operations
#Generate Account Funtions
#Use functions

import datetime
import random

datetime_object = datetime.datetime.now()
def accountCreator():
    return random.randrange(1111111111,9999999999)

userAccountInfo ={}

def init():
    print(datetime_object)
    print('Welcome to Global Bank')
    print('Do you have an account with us? \n')
    accountStatus = int(input(' Select (1) yes, login (2) no, Register, (3) no, Exit  \n'))
    if(accountStatus == 1):
        login()
    elif(accountStatus == 2):
        register()
    else: print ('Exit')
        

def login():
    print('To login into account enter username')
    username = input("\n")
    print(' Hello %s \n' % username)
    password = input(' Enter password \n')
    print(' %s how can we help you today?' % username)
    operations()
        
def operations():
    print('1.Withdrawl')
    print('2.Cash Deposit')
    print('3.Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option: \n'))
    if(selectedOption == 1):
            print('you selected %s' %selectedOption)
            withdrawal = int(input('How much would you like to withdraw?'))
            if(withdrawal >= 10):
                print('Please take your $ %s' % withdrawal)
                transactionCompleted()
            elif(withdrawal < 10):
                print('Cannot withdraw less than $10')
                
            else:
                print('Invalid Option')

    elif(selectedOption == 2):
            print('you selcted %s' %selectedOption)
            deposit = int(input('How much would you like to deposit?'))
            print('Current balance is $ %s' % deposit)
            print(' How else can we serve you?')
            operations()
            while(deposit < 0):
                print('return to main menu')
                operations()
            
    elif(selectedOption == 3):
            print('you selcted %s' %selectedOption)
            complaint = input('What issue would you like to report?')
            print("%s , We will review the issue shortly." %complaint)
            print('Thank you for contacting us. How else can we serve you?')
            operations()
            
    elif(selectedOption == 4):
            login()
    else:
        print('Invalid option selected, please try again')
        operations()

def register ():
    print('Welcome to registration')
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")
    accountNumber = accountCreator()
    accountNumber = ('Your account number is %s' % accountNumber)

    userAccountInfo[accountNumber] = [ first_name, last_name, email, password ]
        
       
    print("Your account has been created")
    print('Your account number is: %s' % accountNumber)
    print('Here are your account details please keep this information confidential %s: ' % userAccountInfo)
    login()
     


init()



